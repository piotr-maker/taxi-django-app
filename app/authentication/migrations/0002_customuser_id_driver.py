# Generated by Django 4.0.5 on 2022-06-09 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='id_driver',
            field=models.BooleanField(default=False),
        ),
    ]
