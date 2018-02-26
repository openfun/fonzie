# -*- coding: utf-8 -*-
"""
Database models for fonzie.
"""

from __future__ import absolute_import, unicode_literals

from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):

    class Meta:
        db_table = 'auth_userprofile'
        managed = False

    user = models.OneToOneField(User, unique=True, db_index=True, related_name='profile')
    name = models.CharField(blank=True, max_length=255, db_index=True)
