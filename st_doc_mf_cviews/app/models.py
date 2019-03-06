# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Student(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    phoneno=models.IntegerField()
    address=models.TextField(max_length=300)

    def __str__(self):
        return self.email

class Documents(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    firstdoc=models.ImageField(upload_to="files",default=False)
    seconddoc=models.ImageField(upload_to="files",default=False)
