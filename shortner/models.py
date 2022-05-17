from pyexpat import model
from django.db import models

# Create your models here.

class URL(models.Model):
    original_url = models.CharField(max_length=500)
    short_url = models.CharField(max_length=5, unique=True)
