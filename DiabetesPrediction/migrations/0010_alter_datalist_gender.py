# Generated by Django 4.0 on 2022-03-04 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DiabetesPrediction', '0009_alter_datalist_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datalist',
            name='Gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
    ]
