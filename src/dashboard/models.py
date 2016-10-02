from django.db import models
from django.conf import settings

class Area(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	name = models.CharField(max_length=100)
	createdtimestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
	modifiedtimestamp = models.DateTimeField(auto_now=True,auto_now_add=False)
	apiurl = models.CharField(max_length=500)
	status = models.CharField(max_length=50)

class TestArea(models.Model):
	field = models.CharField(max_length=1)
	newfield1 = models.CharField(max_length=2, null=True)
	newfield2 = models.CharField(max_length=2, null=True)