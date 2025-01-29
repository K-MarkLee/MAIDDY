<<<<<<< HEAD
=======
from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager): 
    def create_user(self, username, email, password=None, **extra_fields):
        if not email: 
            raise ValueError('이메일이 필요합니다.')
        
        if not username: 
            raise ValueError('유저이름이 필요합니다.')

        user = self.model( 
            email=self.normalize_email(email),  
            username=username,  
            **extra_fields 
        )

        user.set_password(password) 
        user.save(using=self._db)  
        return user


    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)  
        extra_fields.setdefault('is_superuser', True)  

        if extra_fields.get('is_staff') is not True:  
            raise ValueError('스태프는 is_staff=True 여야 합니다.')
        
        if extra_fields.get('is_superuser') is not True:  
            raise ValueError('관리자는 is_superuser=True 여야 합니다.')

        return self.create_user(email=email, username=username, password=password, **extra_fields)


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=50, unique=True)  
    username = models.CharField(max_length=30, unique=True, validators=[MinLengthValidator(3)])  

    objects = UserManager()  

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['username']  

    def __str__(self):
        return self.username
>>>>>>> mvp
