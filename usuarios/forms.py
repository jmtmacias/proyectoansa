from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from usuarios.models import Banco, Perfil

class BancoForm(ModelForm):
	class Meta:
		model = Banco

class PerfilForm(ModelForm):
	user = forms.CharField(max_length=50)
	class Meta:
		CHOICES = Banco.objects.all()
		model = Perfil
		fields = ("user","telefono","avatar","banco","cuenta")
		widgets = {'banco': forms.Select(attrs={'class':'form-control'},choices=CHOICES )}
		


class UserCreateForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "first_name","last_name", "password1", "password2","is_staff","is_active")

	def save(self, commit=True):
		user = super(UserCreateForm, self).save(commit=False)
		user.email = self.cleaned_data["email"]
		if commit:
			user.save()
		return user