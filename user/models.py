from django.db import models
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser
from .managers import CustomBaseUser

class User(AbstractBaseUser,PermissionsMixin):
   
    username        = models.CharField(max_length=50,unique=True)
    email           = models.EmailField(max_length=100,unique=True)
    full_name       = models.CharField(max_length=50)
    
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    
    objects         = CustomBaseUser()
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username','name']

    def __str__(self):
        return self.email

   
