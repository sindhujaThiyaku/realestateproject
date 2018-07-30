# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
'''
    06-Feb-2018 || SKT || BaseModel creation
    07-Feb-2018 || JAN || V1- created_date,modified_date- field modified with auto_now_add and auto_now respectively
    09-Feb-2018 || ANT || V2- RoleInfo, PermissionInfo, GroupPermissionRelationShip, MenuRolePermissionRelationShip created
    09-Feb-2018 || ANT || V3- Removed refitem_category_id in Reference_Item_Category. Rename the refitems_category_id to refitems_category
    30-May-2018 || ANT || V3- country code add in country modal
'''
class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)#auto_now_add is included-JAN-07Feb2018
    created_by = models.ForeignKey(User,related_name="created_by_%(app_label)s_%(class)s_related",blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True,blank=True, null=True)#auto_now is included-JAN-07Feb2018
    modified_by = models.ForeignKey(User,related_name="modified_by_%(app_label)s_%(class)s_related",blank=True, null=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        abstract = True
        
# This code is triggered whenever a new user has been created and saved to the database
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.
mobile_number = models.CharField('Mobile Number',max_length=100,null=True)
mobile_number.contribute_to_class(User, "mobile_number")
