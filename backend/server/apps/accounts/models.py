from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

#from organizations.mixins import OrganizationMixin
from organizations.models import Organization


from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import UserManager
import django

class MyUserManager(UserManager):
    pass

class MyUser(AbstractUser):
    email = models.EmailField(blank=False, max_length=254, verbose_name='email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = MyUserManager()

class MyOrganization(Organization):
    special_description = models.TextField()
