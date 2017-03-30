from __future__ import unicode_literals
from django.db import models
from accounts.models import User
#from django.contrib.auth import get_user_model
#User = get_user_model()

# Create your models here.
class Posting(models.Model):
	user = models.ForeignKey(User, unique=False)
	posting_text = models.CharField(max_length=200)
	company_name = models.CharField(max_length=200)
	job = models.CharField(max_length=200)
	job_description = models.CharField(max_length=1000)
	def __str__(self):
		return "Company Name: " + self.company_name + "\n" + "Job: " + self.job + "\n" + "Job Description: " + self.job_description

class Founder(models.Model):
	posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField()
	university = models.CharField(max_length=50)
	def  __str__(self):
		return self.email



