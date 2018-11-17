
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
print(User)
print('pk', User._meta.pk.name)

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

        #if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
        #raise serializers.ValidationError({'org': 'no no'})

        user = User(username=username, email=email, password=password)

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
        except IntegrityError as e:
            print('fail', str(e))
            self.fail('cannot_create_user')

        return user

    def perform_create(self, validated_data):
        with transaction.atomic():
            print('serializer perform_create')
            organization = validated_data.get('organization')
            print('org', organization)
            print(validated_data)

            user_validated_data = {'username': validated_data.get('username'),
                                    'email': validated_data.get('email'),
                                    'password': validated_data.get('password')}
            user = User.objects.create_user(**user_validated_data)

            if settings.SEND_ACTIVATION_EMAIL:
                user.is_active = False
                user.save(update_fields=['is_active'])
        return user
