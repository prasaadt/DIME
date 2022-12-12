from django.db import models

# Create your models here.
class Faculty(models.Model):
    fno=models.IntegerField()
    Fname=models.CharField(max_length=30)
    Flastname=models.CharField(max_length=30)
    Fdes=models.CharField(max_length=20)

def __str__(self):
    return 'Faculty object with fno: +str(self.no)'
