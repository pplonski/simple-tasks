
import warnings

from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.db import IntegrityError, transaction

from rest_framework import exceptions, serializers

from djoser import constants, utils
from djoser.compat import get_user_email, get_user_email_field_name
from djoser.conf import settings

User = get_user_model()
from .models import MyOrganization

from organizations.utils import create_organization


class MyUserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True
    )

    username = serializers.CharField(
        write_only=True,
        required=True
    )

    organization = serializers.CharField(write_only=True, required=True)

    default_error_messages = {
        'cannot_create_user': constants.CANNOT_CREATE_USER_ERROR,
    }

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'organization')
        #fields = tuple(User.REQUIRED_FIELDS) + (
        #    User.USERNAME_FIELD, User._meta.pk.name, 'password' #, 'organization'
        #)

    def validate(self, attrs):
        print('serializer validate', attrs)
        #print(**attrs)
        organization = attrs.get('organization')

        username = attrs.get('username')
        email = attrs.get('email')
        password = attrs.get('password')


        user = User(username=username, email=email, password=password)

        #my_org = MyOrganization(name=organization)
        #print('slug', my_org.slug)
        #print(my_org)
        #if MyOrganization.objects.get(slug=my_org.slug).exists():
        #    raise serializers.ValidationError({'organization': 'Already exists'})

        #print('my_org', my_org)

        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            raise serializers.ValidationError({'password': list(e.messages)})

        return attrs

    def create(self, validated_data):
        try:
            print('serializer.create')
            print(validated_data)
            user = self.perform_create(validated_data)
            print('----')

        except IntegrityError as e:
            print('fail', str(e))
            self.fail('cannot_create_user')

        return user

    def perform_create(self, validated_data):
        print('srializers perform_create')
        with transaction.atomic():

            organization = validated_data.get('organization')

            user_validated_data = {'username': validated_data.get('username'),
                                    'email': validated_data.get('email'),
                                    'password': validated_data.get('password')}
            user = User.objects.create_user(**user_validated_data)

            #my_org = create_organization(user, organization)
            my_org = MyOrganization(name=organization)
            my_org.save()
            print(my_org)
            #print(my_org.slug)

            orgs = MyOrganization.objects.all()
            print(orgs)
            for o in orgs:
                print('>', o, o.name)


            if settings.SEND_ACTIVATION_EMAIL:
                user.is_active = False
                user.save(update_fields=['is_active'])
        return user
