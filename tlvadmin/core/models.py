from django.db import models
from django.contrib.auth.models import AbstractUser

#Extend User Model 
class User(AbstractUser):
    date_modified = models.DateTimeField(auto_now=True)