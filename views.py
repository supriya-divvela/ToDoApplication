from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Todo

def index(request):
    todos = Todo.objects.all()
    context = {
        'todos':todos
    }
    return render(request, 'index.html', context)

def details(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo':todo
    }
    return render(request, 'details.html', context)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        todo = Todo(title=title, text=text)
        todo.save()

        return redirect('/')
    else:
        return render(request, 'add.html')


def deleterecord(request,id):
    if request.method=="POST":
        todo=Todo.objects.get(id=id)
        todo.delete()
        return redirect('/')
    else:
        return render(request,'delete.html')


def updaterecord(request,id):
    if(request.method=="POST"):
        title=request.POST['title']
        text=request.POST['text']
        todo=Todo.objects.filter(id=id).update(title=title,text=text)
        return redirect('/')
    else:
        return render(request,'update.html')