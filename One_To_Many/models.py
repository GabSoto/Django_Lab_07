from django.db import models

# Create your models here.

class CEO(models.Model):
    name = models.CharField(max_length=30)

class companies(models.Model):
    name = models.CharField(max_length=40)
    ceo = models.ForeignKey(CEO, on_delete=models.CASCADE)