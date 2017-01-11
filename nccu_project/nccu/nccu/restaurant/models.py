from django.db import models
from nccu.settings import *
from django.contrib.auth.models import User

# Create your models here.

class Restaurant(models.Model):
	name = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=20,null=True,blank=True)
	address = models.CharField(max_length=100,null=True,blank=True)
	opentime = models.CharField(max_length=50,null=True,blank=True)
	longitude = models.FloatField(null=True,blank=True,default=None)
	latitude = models.FloatField(null=True,blank=True,default=None)
	def __str__(self):
		return self.name

class Food(models.Model):
	menu = models.ImageField(upload_to=MENU_PIC,height_field=None,width_field=None,max_length=100,null=True,blank=True)
	restaurant=models.ForeignKey(Restaurant)

	def __str__(self):
		return self.menu

class Comment(models.Model):
	content=models.CharField(max_length=255)
	user=models.CharField(max_length=255)
	date_time=models.DateTimeField()
	restaurant=models.ForeignKey(Restaurant)
