from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator

class MyUserManager(UserManager):
    pass

class MyUser(AbstractUser):
    email = models.EmailField(blank=False, max_length=254, verbose_name='email address', unique=True)
    username = models.CharField(help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                max_length=150, unique=False,
                validators=[UnicodeUsernameValidator()],
                verbose_name='username')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = MyUserManager()

class MyOrganization(models.Model):
    name = models.CharField(max_length=200, help_text='The name of the organization',
                            blank=False, null=False,
                            validators=[UnicodeUsernameValidator()])
    slug = models.CharField(max_length=200, unique=True, blank=False, null=False,
                            validators=[UnicodeUsernameValidator()],)
    is_active = models.BooleanField(default=True)
    monthly_subscription = models.IntegerField(default=1000)
    

#class AccountOwner(OrganizationOwnerBase):
#    pass
