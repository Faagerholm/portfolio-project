# Generated by Django 2.0.2 on 2018-04-12 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]