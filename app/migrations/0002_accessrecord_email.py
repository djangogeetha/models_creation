# Generated by Django 4.2.3 on 2023-08-17 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessrecord',
            name='email',
            field=models.EmailField(default='geetha@gmail.com', max_length=254),
        ),
    ]
