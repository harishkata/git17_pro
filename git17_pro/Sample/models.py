from django.db import models

# Create your models here.

class Sampl(models.Model):
    name = models.CharField(max_length=15)