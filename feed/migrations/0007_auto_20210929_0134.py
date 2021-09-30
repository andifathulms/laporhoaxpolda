# Generated by Django 3.2.7 on 2021-09-28 18:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0006_auto_20210929_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='feed',
            name='imgpath',
            field=models.CharField(blank=True, default='20210929-013456', max_length=200),
        ),
    ]
