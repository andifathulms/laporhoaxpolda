# Generated by Django 3.2.7 on 2021-10-05 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0014_auto_20211005_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='img_b64',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feed',
            name='imgpath',
            field=models.CharField(blank=True, default='20211005-180605', max_length=200),
        ),
    ]
