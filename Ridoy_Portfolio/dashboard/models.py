from django.db import models
from django.contrib.auth.models import AbstractUser, User, BaseUserManager, AbstractBaseUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)

    # add any additional fields you need for your user model

    # set the email field as the unique identifier for the user
    USERNAME_FIELD = 'email'

    # set the fields required to create a user account
    REQUIRED_FIELDS = ['username']