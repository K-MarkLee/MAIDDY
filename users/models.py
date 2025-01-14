from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser, BaseUserManager


class GenderChoices(models.TextChoices):
    MALE = 'M', '남성'
    FEMALE = 'F', '여성'
    NONE = 'NONE', '답변하지 않음'
    
    
    
# 사용자 생성 및 관련 메서드 정의하는 모델 매니저 
# 메서드는 create_user와 create_superuser
# 일반 사용자 및 관리자 계정을 생성할 것.

class UserManager(BaseUserManager): 
    def create_user(self, username, email, password=None, **extra_fields): # password=None은 기본값이 None이라는 뜻 / **extra_fields는 추가 필드를 받기 위함
        if not email:  # 이메일이 없는 경우 에러 발생
            raise ValueError('이메일이 필요합니다.')
        
        if not username:  # 사용자 이름이 없는 경우 에러 발생생
            raise ValueError('유저이름이 필요합니다.')

        user = self.model( # 사용자 생성
            email=self.normalize_email(email),  # 이메일 소문자로 변경
            username=username,  # 사용자 이름
            **extra_fields # 추가 필드
        )

        user.set_password(password)  # 비밀번호 설정(암호화)
        user.save(using=self._db)  # DB에 저장(여러 데이터베이스를 사용하는 경우 필요)
        return user


    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)  # 스태프 권한 부여
        extra_fields.setdefault('is_superuser', True)  # 슈퍼유저 권한 부여

        if extra_fields.get('is_staff') is not True:  # 스태프 권한이 없는 경우
            raise ValueError('스태프는 is_staff=True 여야 합니다.')
        
        if extra_fields.get('is_superuser') is not True:  # 슈퍼유저 권한이 없는 경우
            raise ValueError('관리자는 is_superuser=True 여야 합니다.')

        return self.create_user(email=email, username=username, password=password, **extra_fields)


# 사용자 모델
class User(AbstractUser):
    email = models.EmailField(max_length=50, unique=True)#이메일 필드
    username = models.CharField(max_length=30, unique=True, validators=[MinLengthValidator(3)]) # 아이디로 사용할 username 필드 / 최소 3글자 이상
    bio = models.TextField(blank=True, null=True) #자기소개(선택)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True) # 프로필 이미지(선택)
    birth_of_date = models.DateField(null=True, blank=True) #생년월일(선택)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices, null=True, blank=True) # 성별(선택)


    objects = UserManager()  # 사용자 매니저 사용
    USERNAME_FIELD = 'email'  # 로그인 시 이메일 사용
    REQUIRED_FIELDS = ['username']  # 필수 입력 필드(email은 기본 제공되기에 생략함)

    def __str__(self):
        return self.username
