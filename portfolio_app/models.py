from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.gis.db import models
# from django.db import models
import os
from django.conf import settings
from datetime import date,datetime
import re

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(null=True,max_length=30)
    phone_number = models.CharField(max_length=20)
    home_address = models.CharField(max_length=255)
    location = models.PointField(null=True, blank=True)
    designation = models.CharField(null=True, blank=True, max_length=50)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name
    


class Project(models.Model):

    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    github_link = models.CharField(max_length=2000)
    tech_stack = models.CharField(max_length=500)
    image = models.FilePathField(path=os.path.join(settings.BASE_DIR, "portfolio_app/static/img"), default="")

    @property
    def image_path(self):
        return re.sub('.*img/','',self.image)

    def __str__(self):
        return self.title

class Experience(models.Model):
    designation = models.CharField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    is_present = models.BooleanField(null=True,blank=True)
    responsibilities_1 = models.CharField(max_length=2000,default=None,blank=True)
    responsibilities_2 = models.CharField(max_length=2000,default=None,blank=True)
    responsibilities_3 = models.CharField(max_length=2000,default=None,blank=True)
    responsibilities_4 = models.CharField(max_length=2000,default=None,blank=True)
    company = models.CharField(max_length=200,default=None,blank=True)
    location = models.CharField(max_length=200,default=None,blank=True)

    def __str__(self):
        return self.designation

class Skill(models.Model):
    name = models.CharField(max_length=50)
    image =models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Connection(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name


