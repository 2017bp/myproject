from __future__ import unicode_literals
from django.db import models
from accounts.models import User
from django.db.models.signals import post_save
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

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user')
    photo = models.FileField(verbose_name="Profile Picture",
                    max_length=255, null=True, blank=True)
    website = models.URLField(default='', blank=True)
    blurb = models.TextField(default='', blank=True)
    phone_number = models.CharField(max_length=20, blank=True, default='')
    city = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=100, default='', blank=True)
    major = models.CharField(max_length=100, default='', blank=True)
    university = models.CharField(max_length=100, default='', blank=True)

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)



