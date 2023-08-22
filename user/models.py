from django.db import models
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser
from .managers import CustomBaseUser

class User(AbstractBaseUser,PermissionsMixin):
   
    username        = models.CharField(max_length=50,unique=True)
    email           = models.EmailField(max_length=100,unique=True)
    USER_ROLES = (
        ('visitor', 'Visitor'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=USER_ROLES, default='staf')
    # required 
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    objects         = CustomBaseUser()
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_superuser
    
    def has_module_perms(self,add_label):
        return True


class OnlineUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username