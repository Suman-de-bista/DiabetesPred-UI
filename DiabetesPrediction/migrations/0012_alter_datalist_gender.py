# Generated by Django 4.0 on 2022-03-04 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DiabetesPrediction', '0011_alter_datalist_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datalist',
            name='Gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10, null=True),
        ),
    ]
