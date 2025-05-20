from django.db import models

# Create your models here.
class Colour(models.Model):
    c_name = models.CharField(max_length=100)


class Person(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    age = models.IntegerField()
    color = models.ForeignKey(Colour, null=True, blank=True, on_delete=models.CASCADE,)

