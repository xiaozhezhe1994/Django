# Generated by Django 2.2 on 2021-09-04 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='info',
            field=models.CharField(default='', max_length=100, verbose_name='描述'),
        ),
    ]
