# Generated by Django 3.1.4 on 2020-12-23 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]
