# Generated by Django 4.0 on 2022-03-04 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DiabetesPrediction', '0008_alter_datalist_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datalist',
            name='Gender',
            field=models.IntegerField(choices=[(0, 'Male'), (1, 'Female')], null=True),
        ),
    ]
