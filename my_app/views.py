from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

# Create your views here.
def index(request):
    board = Board.objects.all()
    return render(request, 'index.html', {'board': board})
