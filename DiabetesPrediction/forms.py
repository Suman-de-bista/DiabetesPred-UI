from cProfile import label
from django import forms
from django.forms import ModelForm,widgets
from .models import Datalist

class DatalistForm(ModelForm):
    CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ]
    Gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect,label='')
    class Meta:
        model = Datalist
        fields = ('FName','LName','Gender','Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age')
        labels = {
            "FName": "",
            "LName": "",
            "Gender": "",
            "Pregnancies": "",
            "Glucose": "",
            "BloodPressure": "",
            "SkinThickness": "",
            "Insulin": "",
            "BMI": "",
            "DiabetesPedigreeFunction": "",
            "Age": "",
        }
        widgets = {
            'FName': forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'First Name'}),
            'LName': forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'Last Name'}),
            'Pregnancies': forms.NumberInput(attrs={'class':'form-control', 'PlaceHolder':'Pregnancies'}),
            'Glucose': forms.NumberInput(attrs={'class':'form-control', 'PlaceHolder':'Glucose'}),
            'BloodPressure': forms.NumberInput(attrs={'class':'form-control', 'PlaceHolder':'BloodPressure'}),
            'SkinThickness': forms.NumberInput(attrs={'class':'form-control', 'PlaceHolder':'SkinThickness'}),
            'Insulin': forms.NumberInput(attrs={'class':'form-control', 'PlaceHolder':'Insulin'}),
            'BMI': forms.NumberInput(attrs={'class':'form-control', 'PlaceHolder':'BMI'}),
            'DiabetesPedigreeFunction': forms.NumberInput(attrs={'class':'form-control', 'PlaceHolder':'DiabetesPedigreeFunction'}),
            'Age': forms.NumberInput(attrs={'class':'form-control', 'PlaceHolder':'Age'}),
        }
