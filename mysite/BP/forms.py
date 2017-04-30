from django import forms
from accounts.models import User
from .models import Posting

class PostForm(forms.ModelForm):
	posting_text = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Posting Description'}))
 	company_name = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Company Name'}))
 	job = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Job'}))
 	job_description = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Job Description'}))
	class Meta:
    		model = Posting
    		fields = ('posting_text', 'company_name', 'job', 'job_description',)



 
class UserForm(forms.ModelForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
 	last_name = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Last Name'}))
 	email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    	class Meta:
        	model = User
        	fields = ['first_name', 'last_name', 'email']