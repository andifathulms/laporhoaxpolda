from django.db import models

from account.models import Account 

import time
import functools

timestr = time.strftime("%Y%m%d-%H%M%S")
def get_profile_image_filepath(self, filename):
	return 'uploads/feed/'+ str(self.author.id) + '/' + timestr + '/index.png'

class Feed(models.Model):
	id = models.BigAutoField(primary_key=True)
	title = models.CharField(max_length = 200)
	content = models.TextField()
	thumbnail = models.ImageField(upload_to=get_profile_image_filepath, default='uploads/feed/index.jpg', blank=True)
	imgpath = models.CharField(max_length = 200, blank=True, default=timestr)
	author = models.ForeignKey(Account, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	view = models.IntegerField(default=0)
	kategori = models.CharField(max_length=100, default="None")

class NewsCategory(models.Model):
	id = models.BigAutoField(primary_key=True)
	name = models.CharField(max_length=100)
