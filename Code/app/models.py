# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Data_source(models.Model):
    name = models.CharField(max_length=55, null=True)

    class Meta:
        db_table = "data_sources"


class Student(models.Model):
    name = models.CharField(max_length=55, null=True)
    number = models.CharField(max_length=55, null=True)
    email = models.EmailField(null=True)
    linkedin = models.CharField(max_length=55, null=True)
    github = models.CharField(max_length=55, null=True)
    gender = models.CharField(max_length=6, null=True)
    education_level = models.CharField(max_length=25, null=True)
    it_background = models.BooleanField(null=True)
    address = models.CharField(max_length=25, null=True)
    data_source = models.ForeignKey(Data_source, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "students"

class ActivityLog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    file_name = models.CharField(max_length=255)
    data_source_name = models.CharField(max_length=255)
    execution_time_in_seconds = models.FloatField()
    number_of_records = models.IntegerField()

    class Meta:
        db_table = "activity_logs"

