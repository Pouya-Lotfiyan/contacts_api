# Generated by Django 3.2.4 on 2021-06-05 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phonenumber',
            name='contact',
        ),
    ]
