from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from datetime import datetime  
# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):
        user = self.model(
            email=self.normalize_email(email),
            is_active=True,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.model(
            email=email,
            is_staff=True,
            is_superuser=True,
            is_active=True,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
        
class User(AbstractBaseUser, PermissionsMixin):
	USERNAME_FIELD='email'
	email = models.EmailField(unique=True)
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
	is_active = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
        date_joined = models.DateTimeField(default=datetime.now, blank=True)

	def get_full_name(self):
		return self.email

	def get_short_name(self):
		return self.email

	objects = UserManager()