from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm

def index(request):
	form = MessageForm(request.POST)
	if request.method == 'POST':
		texto = request.POST['message']
		if form.is_valid():
			form.save()
			return redirect('index')
			print(texto)
		else:
			form = MessageForm()
	return render(request, 'index.html', {'form':form})