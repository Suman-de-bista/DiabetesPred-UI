# Generated by Django 4.0 on 2022-03-04 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DiabetesPrediction', '0006_remove_datalist_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='datalist',
            name='Gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
    ]
