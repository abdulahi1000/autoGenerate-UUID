# Generated by Django 3.1.4 on 2021-05-24 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
