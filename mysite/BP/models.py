from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Posting(models.Model):
	company_name = models.CharField(max_length=200)
	job = models.CharField(max_length=200)
	job_description = models.CharField(max_length=1000)

class Founder(models.Model):
	posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField()
	university = models.CharField(max_length=50)


