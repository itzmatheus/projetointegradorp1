from django import forms
from django.forms import ModelForm
from .models import Message

class MessageForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(
		attrs={'class': 'form-control'}), label='Nome Completo')
	email = forms.EmailField(widget=forms.EmailInput(
		attrs={'class':'form-control'}),required=False, label='Email')
	title = forms.CharField(widget=forms.TextInput(
		attrs={'class':'form-control'}), label='Titulo da menssagem')
	message = forms.CharField(widget=forms.TextInput(
		attrs={'class':'form-control'}), label='Mensagem')

	class Meta:
		model = Message
		fields = ['name', 'email', 'title', 'message']