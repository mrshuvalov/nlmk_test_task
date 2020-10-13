from django.db import models

# Create your models here.

class Table(models.Model):
    x_axis = models.IntegerField(verbose_name="X")
    y_axis = models.IntegerField(verbose_name="Y")
    value = models.TextField(verbose_name="Value")
