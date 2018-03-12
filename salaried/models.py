import copy
import os
import uuid

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone

# Create your models here.


# Salaied model
from bu.models import BU


class Salaried(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    cin_code = models.CharField(max_length=10, unique=True)
    birth_day = models.DateField()
    hire_day = models.DateField()
    email = models.EmailField(max_length=100, blank=False, unique=True)
    cnss_code = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    bu = models.ForeignKey(BU, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        # verbose_name_plural = "Posts"
        ordering = ["-created_at"]


class Document(models.Model):
    def user_directory_path(instance, filename):
        filename, file_extension = os.path.splitext(filename)
        return 'documents/user_{0}/{1}_{2}{3}'.format(instance.salaried.id, instance.label, uuid.uuid4(),
                                                      file_extension)

    label = models.CharField(max_length=20)
    description = models.TextField()
    attached_piece = models.FileField(upload_to=user_directory_path, validators=[FileExtensionValidator(['pdf','doc','docx','jpg','jpeg','png'])])
    salaried = models.ForeignKey(Salaried, on_delete=models.CASCADE)
