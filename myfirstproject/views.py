from django.http import HttpResponse
from django.shortcuts import render

def about(request):
	return HttpResponse('This is about a page')

def home(request):
	return render(request, 'home.html', {'greeting':'Hello!'})