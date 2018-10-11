# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Followmessage(models.Model):
    id = models.IntegerField(blank=True, null=True)
    messageid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    picpath = models.CharField(max_length=100, blank=True, null=True)
    postdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'followmessage'


class Message(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    picpath = models.CharField(max_length=100, blank=True, null=True)
    postdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message'


class Message1(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    picpath = models.CharField(max_length=100, blank=True, null=True)
    postdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message1'


class User(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
    def __str__(self):
        return  self.name