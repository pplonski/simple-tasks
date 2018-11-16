from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

#from organizations.mixins import OrganizationMixin
from organizations.models import Organization

class MyUser(AbstractUser):
    email = models.EmailField(blank=True, max_length=254, verbose_name='email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]
    #REQUIRED_FIELDS = ['email', 'username']

class MyOrganization(Organization):
    special_description = models.TextField()
