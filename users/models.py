from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email: # 이메일이 입력되지 않았을 경우
            raise ValueError("회원가입시 이메일이 필요합니다.")
        
        if not username: # 이름이 입력되지 않은 경우
            raise ValueError("회원가입시 이름이 필요합니다.")


        email = self.normalize_email(email) # 소문자 변경
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db) # 여러 데이터베이스에 사용 가능
        return user
    

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("관리자는 is_superuser=True로 설정해야 합니다.")
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError("스태프는 is_staff=True로 설정해야 합니다.")
        

        return self.create_user(email, username, password, **extra_fields)
    


class User(AbstractUser, PermissionsMixin): 
    email = models.EmailField(unique=True)  # 이메일 필드 (아이디로 사용)
    username = models.CharField(max_length=30, unique=True, validators=[MinLengthValidator(3)])  # MinLengthValidator(3)은 최소 3글자 이상
    birth_date = models.DateField()  # 생년월일 필드
    gender = models.CharField(max_length=10, blank=True, null=True)  # 성별 필드
    bio = models.TextField(blank=True, null=True)  # 자기소개 필드
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)  # 프로필 이미지

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # username을 로그인 필드로 사용
    REQUIRED_FIELDS = ['email', 'username']  # 필수 입력 필드 설정

    def __str__(self):
        return self.username



