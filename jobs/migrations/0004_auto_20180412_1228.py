# Generated by Django 2.0.2 on 2018-04-12 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20180412_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=models.TextField(max_length=300),
        ),
    ]