# Generated by Django 4.0 on 2022-03-04 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DiabetesPrediction', '0003_user_remove_datalist_gender_remove_datalist_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='Name',
            field=models.CharField(max_length=32),
        ),
    ]
