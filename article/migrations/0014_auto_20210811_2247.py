# Generated by Django 3.1.3 on 2021-08-11 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_auto_20210811_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='content',
            field=models.ImageField(upload_to='avatar/%Y%m%d'),
        ),
    ]
