# Generated by Django 3.2.7 on 2021-10-05 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0012_alter_feed_imgpath'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='kategori',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='feed',
            name='imgpath',
            field=models.CharField(blank=True, default='20211005-134110', max_length=200),
        ),
    ]
