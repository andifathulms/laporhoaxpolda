# Generated by Django 3.2.7 on 2021-10-05 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0015_auto_20211005_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='imgpath',
        ),
        migrations.AlterField(
            model_name='feed',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='feeds/'),
        ),
    ]