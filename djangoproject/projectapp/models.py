from django.db import models


# Create your models here.
class Place(models.Model):
    Name = models.CharField(max_length=250)
    Image = models.ImageField(upload_to='pic')
    Desc = models.TextField()

    def __str__(self):
        return self.Name

class Persons(models.Model):
    Name = models.CharField(max_length=250)
    Image = models.ImageField(upload_to='pic1')
    Desc = models.TextField()

    def __str__(self):
        return self.Name

