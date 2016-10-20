from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Users(models.Model):
#id = models.CharField(max_length=30)
	firstname = models.CharField(max_length=45);
	lastname = models.CharField(max_length=45);
	middlename = models.CharField(max_length=45);
	gender = models.CharField(max_length=45);
	dateofB = models.CharField(max_length=45);

	class Meta:
		db_table = "person";

