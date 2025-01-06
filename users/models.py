from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

# 사용자 생성 및 관련 메서드 정의하는 모델 매니저 
# 메서드는 create_user와 create_superuser
# 일반 사용자 및 관리자 계정을 생성할 것.
class UserManager(BaseUserManager): 
    def create_user(self, username, email, password=None, gender=None, bio=None, birth_of_date=None, **extra_fields): 
        if not email:  # 이메일이 없는 경우 에러 발생
            raise ValueError('Must have user email.')
        if not username:  # 사용자 이름이 없는 경우 에러 발생생
            raise ValueError('Must have user username.')

        user = self.model(
            email=self.normalize_email(email),  # 이메일 소문자로 변경
            username=username,
            gender=gender,
            bio=bio,
            birth_of_date=birth_of_date,
            **extra_fields
        )

        user.set_password(password)  # 비밀번호 설정(암호화)
        user.save(using=self._db)  # DB에 저장(여러 데이터베이스를 사용하는 경우 필요)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)  # 스태프 권한 부여
        extra_fields.setdefault('is_superuser', True)  # 슈퍼유저 권한 부여

        if extra_fields.get('is_staff') is not True:  # 스태프 권한이 없는 경우
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:  # 슈퍼유저 권한이 없는 경우
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email=email, username=username, password=password, **extra_fields)

# 사용자 모델
# AbstractUser를 상속받아서 아래 것들 추가
class User(AbstractUser, PermissionsMixin):
    class GenderChoices(models.TextChoices):  # 성별 선택
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        NONE = 'NONE', 'Prefer not to answer' #이거 한글로 적으면 안되나요?

    email = models.EmailField(max_length=50, unique=True)  #이메일 필드
    username = models.CharField(max_length=30, unique=True, validators=[MinLengthValidator(3)])  # 아이디로 사용할 username 필드 / 최소 3글자 이상
    birth_of_date = models.DateField(null=True, blank=True)  #생년월일(선택)
    bio = models.TextField(blank=True, null=True)  #자기소개(선택)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)  # 프로필 이미지(선택)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices, null=True, blank=True)  # 성별(선택)

    objects = UserManager()  # UserManager 사용

    USERNAME_FIELD = 'email'  # 로그인 시 이메일 사용
    REQUIRED_FIELDS = ['username']  # 필수 입력 필드(email은 기본 제공되기에 생략함)

    def __str__(self):
        return self.username
