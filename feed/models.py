from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from pathlib import Path

from account.models import Account 

import time
import functools
import base64

timestr = time.strftime("%Y%m%d-%H%M%S")
def get_profile_image_filepath(self, filename):
	return 'uploads/feed/'+ str(self.author.id) + '/' + timestr + '/index.png'

class Feed(models.Model):
	id = models.BigAutoField(primary_key=True)
	title = models.CharField(max_length = 200)
	content = models.TextField()
	thumbnail = models.ImageField(upload_to='feeds/', blank=True)
	#img_b64 = models.BinaryField(blank=True, null=True)
	img_b64 = models.TextField(blank=True, null=True)
	author = models.ForeignKey(Account, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	view = models.IntegerField(default=0)
	kategori = models.CharField(max_length=100, default="None")
	
	def save(self):
		if(self.thumbnail.file):
			temp = base64.b64encode(self.thumbnail.file.read())
			self.img_b64 = temp.decode('utf-8')
			return super().save()
		return super().save()

class NewsCategory(models.Model):
	id = models.BigAutoField(primary_key=True)
	name = models.CharField(max_length=100)
