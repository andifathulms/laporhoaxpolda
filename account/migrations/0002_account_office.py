# Generated by Django 3.2.7 on 2021-10-04 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='office',
            field=models.CharField(default='None', max_length=50),
        ),
    ]
