from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.db import models
from django.contrib.auth.models import  AbstractUser, Group
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import  BaseUserManager
from django.utils import timezone

# Group.add_to_class('employee_access_flag', models.BooleanField(default=True))

class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email, 
            last_login=now,
            date_joined=now,
             
            **extra_fields
    )
    
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
#
class User(AbstractBaseUser,PermissionsMixin):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    full_name = models.CharField(max_length=254, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

  

 