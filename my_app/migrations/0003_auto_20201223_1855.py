# Generated by Django 3.1.4 on 2020-12-23 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20201223_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='load_num',
        ),
        migrations.RemoveField(
            model_name='board',
            name='pickup_num',
        ),
        migrations.AddField(
            model_name='board',
            name='broker',
            field=models.CharField(default='', editable=False, max_length=500),
        ),
        migrations.AddField(
            model_name='board',
            name='delivery',
            field=models.CharField(default='', editable=False, max_length=2080),
        ),
        migrations.AddField(
            model_name='board',
            name='load_number',
            field=models.CharField(default='', editable=False, max_length=255),
        ),
        migrations.AddField(
            model_name='board',
            name='mile',
            field=models.CharField(default='', editable=False, max_length=2080),
        ),
        migrations.AddField(
            model_name='board',
            name='origin',
            field=models.CharField(default='', editable=False, max_length=2080),
        ),
        migrations.AddField(
            model_name='board',
            name='pickup_number',
            field=models.CharField(default='', editable=False, max_length=255),
        ),
        migrations.AddField(
            model_name='board',
            name='rate',
            field=models.CharField(default='', editable=False, max_length=2080),
        ),
        migrations.AlterField(
            model_name='board',
            name='dispatch',
            field=models.CharField(default='', editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='board',
            name='driver',
            field=models.CharField(default='', editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='board',
            name='phone_number',
            field=models.CharField(default='', editable=False, max_length=1000),
        ),
    ]
