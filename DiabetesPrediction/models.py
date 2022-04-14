from django.db import models
from django import forms

#creating models here

class Datalist(models.Model):
    CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    FName = models.CharField(max_length=32, null=True)
    LName = models.CharField(max_length=32, null=True)
    Gender = models.CharField(max_length=1, choices=CHOICES)
    Pregnancies = models.IntegerField(max_length=2)
    Glucose = models.IntegerField(max_length=4)
    BloodPressure = models.IntegerField(max_length=4)
    SkinThickness = models.IntegerField(max_length=4)
    Insulin = models.IntegerField(max_length=4)
    BMI = models.FloatField()
    DiabetesPedigreeFunction = models.FloatField()
    Age = models.IntegerField(max_length=3)
    Outcome = models.BooleanField()
    