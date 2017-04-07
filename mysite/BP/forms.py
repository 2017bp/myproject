from django import forms

from .models import Posting

class PostForm(forms.ModelForm):

    class Meta:
        model = Posting
        fields = ('posting_text', 'company_name', 'job', 'job_description',)
