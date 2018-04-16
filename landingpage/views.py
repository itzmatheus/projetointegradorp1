from django.shortcuts import render, redirect
from .forms import MessageForm

def index(request):
	form = MessageForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('index')
		else:
			form = MessageForm()
	return render(request, 'index.html', {'form':form})