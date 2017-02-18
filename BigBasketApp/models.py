from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.contrib.auth.hashers import (
    check_password, make_password, is_password_usable)
from django.core.urlresolvers import reverse
from django.db.models import *
from django.db import migrations
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import models as auth_models
from django.db import models as models
from django.http import JsonResponse
# from rest_framework import status
import uuid
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)
from django.conf import settings
from django.utils import timezone
# Create your models here.

class MyUserManager(BaseUserManager):
    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)

    def set_password(self, email=None, role=None, password=None):     # Sets/updates a user's password when email id is provided
        if not email or not role or not password:
            return JsonResponse({"message": "Invalid email address"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                # role_obj = Role.objects.get(id=role)
                user_obj = User.objects.get(email=email, user_role=role)
            except:
                return JsonResponse({"message": "bad request"}, status=status.HTTP_400_BAD_REQUEST)
            try:
                user_obj.password = make_password(password)
                user_obj.save()
                return JsonResponse({"message":"successfully set the password"}, status=status.HTTP_200_OK)
            except:
                return JsonResponse({"message": "Internal error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_by_natural_key(self, username):
        return self.get(**{'email': username})


class Role(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)


class User(AbstractBaseUser, PermissionsMixin, models.Model):

    # Fields
    objects = MyUserManager()
    email =  CharField(max_length=255, blank=True, null=True,unique=True)
    # created_at = DateTimeField(auto_now=True)
    is_staff = BooleanField(default=False)
    is_active = IntegerField(default=1)
    date_joined = DateTimeField(auto_now=True)
    is_admin = BooleanField(default=False)
    user_role = models.ForeignKey(Role, db_column='user_role', blank=True, null=True)
    USERNAME_FIELD = 'email'


    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.id

    def get_absolute_url(self):
        return reverse('main_role_detail', args=(self.id,))

    def get_update_url(self):
        return reverse('main_role_update', args=(self.id,))

    def get_full_name(self):
        pass

    def get_short_name(self):
        pass


class Category(models.Model):
	name=models.CharField(max_length=64,null=False,blank=True)
	is_active = models.BooleanField(default=True)

class Subcategory(models.Model):
	name=models.CharField(max_length=255,null=False,blank=True)
	is_active=models.BooleanField(default=True)
	fk_category=models.ForeignKey('Category',null=True,blank=False)

class Item(models.Model):
	name=models.CharField(max_length=255,null=False,blank=False)
	fk_subcategory=models.ForeignKey('Subcategory')
	price=models.FloatField(default=0.0)
	featureimage = models.FileField(upload_to='item_images/',blank=True,null=True)
	description = models.TextField()
	is_active=models.BooleanField(default=True)





