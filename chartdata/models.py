from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save

from django.dispatch import receiver

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    population = models.PositiveIntegerField()
    

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length=500,blank=True)
    location = models.CharField(max_length=30,blank=True)
    birth_date = models.DateField(null=True,blank=True)

class Passengers(models.Model):
    name = models.CharField(max_length=122)
    sex = models.CharField(max_length=122)
    survived = models.BooleanField()
    age = models.FloatField()
    ticket_class = models.PositiveSmallIntegerField()
    embarked = models.CharField(max_length=122)