# Generated by Django 3.0.7 on 2020-09-12 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20200912_0616'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(max_length=100)),
                ('user_password', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='LoginModel',
        ),
    ]