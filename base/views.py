from django.shortcuts import render

rooms = [{'id':1, 'name':'room1'},{'id':2, 'name':'room1'},{'id':3, 'name':'room3'}]

def home(request):
    return render(request, 'home.html',{'rooms':rooms})

def room(request):
    return render(request, 'room.html')
