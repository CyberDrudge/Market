from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, full_name, email, password, phone_number=None, is_staff=False, is_admin=False):
        if not username:
            raise ValueError("User must have an username.")
        if not password:
            raise ValueError("User must have a password.")

        user_obj = self.model(
            username=username,
            full_name=full_name,
            email=self.normalize_email(email),
            phone_number=phone_number
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, username, full_name, email, password, phone_number=None):
        user = self.create_user(username, full_name, email, password, phone_number=phone_number, is_staff=True)
        return user

    def create_superuser(self, username, full_name, email, password, phone_number=None):
        user = self.create_user(username, full_name, email, password, phone_number=phone_number, is_staff=True, is_admin=True)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=120, unique=True)
    phone_number = models.CharField(max_length=120, blank=True, null=True)
    username = models.CharField(max_length=120, unique=True)
    full_name = models.CharField(max_length=120)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'full_name']    # Username field and password are required by default

    objects = UserManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
