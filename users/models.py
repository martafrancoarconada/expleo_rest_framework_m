from django.db import models
from django.contrib.auth.models import AbstractUser

#create models here

class User(AbstractUser):
    email = models.EmailField(unique=True)
    
    linkedin = models.CharField(max_length=255, blank=True)
    
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS=[]
    
    
    
    
