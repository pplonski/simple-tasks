from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

from django.db import models
from django.utils.timezone import now
from django.template.defaultfilters import slugify

class AutoCreatedField(models.DateTimeField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('editable', False)
        kwargs.setdefault('default', now)
        super(AutoCreatedField, self).__init__(*args, **kwargs)

class AutoLastModifiedField(AutoCreatedField):
    def pre_save(self, model_instance, add):
        value = now()
        setattr(model_instance, self.attname, value)
        return value

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, username=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
            username='superuser'
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class MyOrganization(models.Model):
    name = models.CharField(max_length=200, help_text='The name of the organization',
                            blank=False, null=False,
                            validators=[UnicodeUsernameValidator()])
    slug = models.CharField(max_length=200, unique=True, blank=False, null=False,
                            validators=[UnicodeUsernameValidator()],)
    is_active = models.BooleanField(default=True)
    monthly_subscription = models.IntegerField(default=1000)
    created_at = AutoCreatedField()
    updated_at = AutoLastModifiedField()

    def save(self, *args, **kwargs):
        # Newly created object, so set slug
        if not self.id:
            self.slug = slugify(self.name)
        super(MyOrganization, self).save(*args, **kwargs)

class MyUser(AbstractUser):
    email = models.EmailField(blank=False, max_length=254, verbose_name='email address', unique=True)
    username = models.CharField(help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                max_length=150, unique=False,
                validators=[UnicodeUsernameValidator()],
                verbose_name='username')

    organizations = models.ManyToManyField(MyOrganization, through='Membership')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = MyUserManager()

class Membership(models.Model):
    statuses = (
        ('admin', 'Admin'),
        ('view', 'View only'),
        ('member', 'Organization member')
    )
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    organization = models.ForeignKey(MyOrganization, on_delete=models.CASCADE)
    status = models.CharField(max_length=32, choices=statuses, default='view', blank=False)
    created_at = AutoCreatedField()
    updated_at = AutoLastModifiedField()



#class AccountOwner(OrganizationOwnerBase):
#    pass
