# Generated by Django 2.0.2 on 2018-04-12 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default='job', max_length=50),
        ),
    ]