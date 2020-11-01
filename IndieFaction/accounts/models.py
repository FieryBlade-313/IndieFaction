
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime
import uuid
from django.utils import timezone


# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):

        if not email:
            raise ValueError("User should have an Email")
        if not username:
            raise ValueError("User should have a Username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):

        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class UserName(models.Model):

    first_name = models.CharField(max_length=20, default='f_name')
    middle_name = models.CharField(max_length=20, default='m_name', blank=True)
    last_name = models.CharField(max_length=20, default='l_name')

    class Meta:
        abstract = True


class Address(models.Model):

    district = models.CharField(max_length=50, default='Sricity')
    state = models.CharField(max_length=50, default='Andhra Pradesh')
    country = models.CharField(max_length=50, default='India')
    pincode = models.BigIntegerField(verbose_name='Pin code', default=600078)

    class Meta:
        abstract = True


class MediaHandles(models.Model):

    facebook = models.URLField(
        verbose_name='Facebook profile', default='www.facebook.com', blank=True)
    linkedin = models.URLField(
        verbose_name='Linkedin profile', default='www.linkedin.com', blank=True)
    instagram = models.URLField(
        verbose_name='Instagram profile', default='www.instagram.com', blank=True)
    github = models.URLField(
        verbose_name='Github profile', default='www.github.com', blank=True)
    discord = models.URLField(
        verbose_name='Discord profile', default='www.discord.com', blank=True)
    website = models.URLField(
        verbose_name='Personal Website', default='www.myprofile.com', blank=True)

    class Meta:
        abstract = True


class IndieUser(AbstractBaseUser, UserName, Address, MediaHandles):
    uid = models.UUIDField(
        default=uuid.uuid4, verbose_name='uid', primary_key=True, editable=False)
    steam_id = models.CharField(
        max_length=50, verbose_name='steam id', unique=True)
    username = models.CharField(max_length=20, unique=True)
    profile_pic = models.ImageField(
        blank=True, default='icon.jpeg', verbose_name='Profile Picture')
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    mobile_no = models.BigIntegerField(
        verbose_name='contact_no', default=1234567890)
    age = models.IntegerField(verbose_name='age', default=18)
    token = models.CharField(
        max_length=50, verbose_name='Token', default='#T', unique=True)
    data_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
