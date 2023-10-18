from django.db import models

# Create your models here.
class Tempdb (models.Model):
	title=models.CharField(max_length=255)
	query=models.CharField(max_length=255)
	description=models.TextField()
	url=models.CharField(max_length=255, unique=True)
	keywords=models.CharField(max_length=255, blank=True, null=True)
	date=models.DateField(blank = True)
