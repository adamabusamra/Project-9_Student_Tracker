# Generated by Django 2.2.10 on 2021-03-26 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210327_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitylog',
            name='number_of_records',
            field=models.FloatField(),
        ),
    ]
