from django.db import models

# Create your models here.
from django.utils import timezone


class BU(models.Model) :
    name = models.CharField(max_length=20)
    manager = models.CharField(max_length=20)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.name
    #class Meta:
        #verbose_name_plural = "Posts"
        #ordering = ["-created_at"]