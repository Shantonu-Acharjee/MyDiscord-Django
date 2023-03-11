from django.shortcuts import render
from django.http import HttpResponse


rooms = [
    {'id' : 1, 'name': 'Lets learn python'},
    {'id' : 2, 'name': 'Lets learn C++'},
    {'id' : 3, 'name': 'Lets learn js'},
]

def home(request):
    return render(request, 'home.html', {'rooms' : rooms})

def room(request):
    return render(request, 'room.html')

