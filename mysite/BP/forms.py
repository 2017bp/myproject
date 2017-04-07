from django import forms
from accounts.models import User
from .models import Posting

class PostForm(forms.ModelForm):

    class Meta:
        model = Posting
        fields = ('posting_text', 'company_name', 'job', 'job_description',)
 
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']