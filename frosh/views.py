from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'frosh/index.html')

def frosh2019(request):
	return render(request, 'frosh/frosh.html')
