from django.db import models
from django.forms import ModelForm
# Create your models here.

class cmanagement(models.Model):
	name = models.CharField(max_length=100)
	details = models.TextField()
	address = models.TextField()
	phone = models.CharField(max_length=20)
	cost = models.IntegerField()

class cmanagementForm(ModelForm):
	class Meta:
		model = cmanagement
		fields = ['name','details','address','phone','cost']	
			
	