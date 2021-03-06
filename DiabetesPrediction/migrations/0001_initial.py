# Generated by Django 4.0 on 2022-02-28 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datalist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pregnancies', models.IntegerField(max_length=2)),
                ('Glucose', models.IntegerField(max_length=4)),
                ('BloodPressure', models.IntegerField(max_length=4)),
                ('SkinThickness', models.IntegerField(max_length=4)),
                ('Insulin', models.IntegerField(max_length=4)),
                ('BMI', models.FloatField()),
                ('DiabetesPedigreeFunction', models.FloatField()),
                ('Age', models.IntegerField(max_length=3)),
                ('Outcome', models.BooleanField()),
            ],
        ),
    ]
