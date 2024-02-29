from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, user_name, password, **extra_fields):
        if not user_name:
            raise ValueError('Tên đăng nhập không được để trống')
        user = self.model(user_name=user_name, password=password, **extra_fields)
        user.save()
        return user

    def create_superuser(self, user_name, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        # if extra_fields.get('is_manager') is not True:
        #     raise ValueError('Superuser must have is_manager=True.')

        return self.create_user(user_name, password, **extra_fields)


class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField('Tên hiển thị',max_length=255)
    name = models.CharField('Tên hiển thị',max_length=255)
    # is_manager = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = []

    username = None
    first_name = None
    last_name = None

    def save(self, *args, **kwargs):
        # if not self.pk:
        #     self.format_code()
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.user_name


