from django.db import models

# Create your models here.

class Blog(models.Model):
    body = models.CharField(max_length=50)
