# Generated by Django 3.2.7 on 2021-09-28 17:29

from django.db import migrations, models
import feed.models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_auto_20210929_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='imgpath',
            field=models.CharField(blank=True, default='20210929-002943', max_length=200),
        ),
    ]
