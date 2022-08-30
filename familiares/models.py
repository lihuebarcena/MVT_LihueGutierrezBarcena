from django.db import models

# Create your models here.


class familiares(models.Model):
    parentesco=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    edad=models.IntegerField()
    year_born=models.DateField()
    