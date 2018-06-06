from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'frosh/index.html')

def frosh2018(request):
	return render(request, 'frosh/frosh.html')
