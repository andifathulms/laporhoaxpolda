from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from pathlib import Path

from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE

from account.models import Account 

class Feed(models.Model):
	id = models.BigAutoField(primary_key=True)
	title = models.CharField(max_length = 200)
	content = HTMLField()
	thumbnail = models.ImageField(upload_to='feeds/', default='feeds/news-default.jpg', blank=True, null=True)
	author = models.ForeignKey(Account, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	view = models.IntegerField(default=0)
	
