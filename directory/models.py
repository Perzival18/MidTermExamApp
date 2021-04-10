from django.db import models

# Create your models here.

class Student(models.Model):
    lastName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.IntegerField()
    course = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='directory/images')

    def __str__(self):
        return self.lastName

class Teacher(models.Model):
    lastName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.IntegerField()
    course = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='directory/images')

    def __str__(self):
        return self.lastName