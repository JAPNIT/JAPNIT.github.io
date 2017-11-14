# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    progress = models.IntegerField(default=0)