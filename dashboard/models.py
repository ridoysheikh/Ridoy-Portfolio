from django.db import models
from django.contrib.auth.models import AbstractUser, User, BaseUserManager, AbstractBaseUser
import datetime

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)

    # add any additional fields you need for your user model

    # set the email field as the unique identifier for the user
    USERNAME_FIELD = 'email'

    # set the fields required to create a user account
    REQUIRED_FIELDS = ['username']

class contacts(models.Model):
    name= models.CharField(max_length=50,null=False,blank=False)
    address = models.CharField(max_length=200,default="Unknown")
    reletion = models.CharField(max_length=50,blank=False)
    phone_number = models.CharField(max_length=20,blank=True)
    email = models.EmailField(blank=True)
    profile_pic = models.ImageField(upload_to='contacts/profile_pic',blank=True)
    fb_id = models.CharField(max_length=200,blank=True)
    last_meet = models.DateField(default=datetime.date.today)
    DOB = models.DateField(blank=True)
    last_contacted = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name
    def delete(self, *args, **kwargs):
        # Delete the image associated with the instance
        self.profile_pic.delete()
        # Call the superclass method
        super().delete(*args, **kwargs)
        
