from django import forms
from accounts.models import User
from .models import Posting, Company

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
 	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
 	email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    	class Meta:
        	model = User
        	fields = ['first_name', 'last_name', 'email']

class CompanyForm(forms.ModelForm):
	company_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Company Name'}))
 	company_description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Description'}))
 	company_link = forms.URLField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Link'}))
 	company_founders = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Founders'}))
 	company_contact_info = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Contact Info'}))
    	class Meta:
        	model = Company
        	fields = ['company_name', 'company_description', 'company_link', 'company_founders', 'company_contact_info', ]