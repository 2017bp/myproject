from django import forms

from .models import User

class RegistrationForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('email', 'first_name', 'last_name',)