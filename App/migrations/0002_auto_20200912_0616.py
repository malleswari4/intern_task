# Generated by Django 3.0.7 on 2020-09-12 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loginmodel',
            old_name='Name',
            new_name='email',
        ),
    ]