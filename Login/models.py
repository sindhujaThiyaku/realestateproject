# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
mobile_number = models.CharField('Mobile Number',max_length=100,null=True)
mobile_number.contribute_to_class(User, "mobile_number")
