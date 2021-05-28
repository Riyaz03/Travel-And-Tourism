from django import forms 
from .models import User,UserLogin,DemoDate

class userdataForm(forms.ModelForm):
	class Meta:
		model=User
		fields="__all__"
		widgets = {'password': forms.PasswordInput(),}

class UserLoginForm(forms.ModelForm):
	class Meta:
		model=UserLogin
		fields="__all__"
		widgets={'password':forms.PasswordInput(),}

class DemoDateForm(forms.ModelForm):
	class Meta:
		model=DemoDate
		fields="__all__"
		widgets = {'demodate': forms.DateInput(),}

