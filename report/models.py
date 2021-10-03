from django.db import models
from account.models import Account

import time

timestr = time.strftime("%Y%m%d-%H%M%S")

def get_profile_image_filepath(self, filename):
	print(self.user.username)
	return 'uploads/report/' + str(self.user.id) + '/' + timestr + '/index.png'


class Report(models.Model):
	id = models.BigAutoField(primary_key=True)
	user = models.ForeignKey(Account, on_delete=models.CASCADE,related_name="user_account")
	url = models.CharField(max_length = 200,blank=True,null=True)
	img = models.ImageField(upload_to=get_profile_image_filepath, default='uploads/report/index.jpg', blank=True,null=True)
	category = models.CharField(max_length = 150)
	status = models.CharField(default="Saved", max_length = 20)
	isAnonym = models.BooleanField(default=False)
	dateReported = models.DateTimeField(auto_now_add=True)
	description = models.CharField(max_length = 150)
	verdict = models.CharField(blank=True,null=True,max_length = 150)
	verdictDesc = models.TextField(blank=True,null=True)
	verdictDate = models.DateTimeField(blank=True,null=True)
	verdictJudge = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True,null=True,related_name="admin_account")


class Category(models.Model):
	id = models.BigAutoField(primary_key=True)
	name = models.CharField(max_length=100)
