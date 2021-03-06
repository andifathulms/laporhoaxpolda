# Generated by Django 3.2.7 on 2021-09-28 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import report.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('img', models.ImageField(blank=True, default='uploads/report/index.jpg', null=True, upload_to=report.models.get_profile_image_filepath)),
                ('category', models.CharField(max_length=150)),
                ('status', models.CharField(default='Saved', max_length=20)),
                ('isAnonym', models.BooleanField(default=False)),
                ('dateReported', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=150)),
                ('verdict', models.CharField(blank=True, max_length=150, null=True)),
                ('verdictDesc', models.TextField(blank=True, null=True)),
                ('verdictDate', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_account', to=settings.AUTH_USER_MODEL)),
                ('verdictJudge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
