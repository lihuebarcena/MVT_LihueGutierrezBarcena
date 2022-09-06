from django.db import models

# Create your models here.


class Familiar(models.Model):
    id=models.IntegerField(primary_key=True,unique=True)
    parentesco=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    edad=models.IntegerField()
    year_born=models.DateField()
    
    def __str__(self):
        return f'{self.name} || {self.edad}'