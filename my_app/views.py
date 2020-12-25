from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
# def index(request):
#     board = Board.objects.all()
#     return render(request, 'index.html', {'board': board})


def home(request):
	update = Update.objects.all()
	context = {'update': update}
	return render(request, 'dashboard.html', context)

def covered(request):
	covered = COVERED_LOAD.objects.all()
	return render(request, 'covered_loads.html', {'covered': covered}) 
