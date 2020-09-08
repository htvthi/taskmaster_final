from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from.forms import *

from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
# Create your views here.

def index(request):
    tasks = Task.objects.all()
    
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/untitled.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form':form}
    return render(request, 'tasks/update.html', context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
    return redirect('/')

    context = {'item':item}
    return render(request, 'tasks/delete.html', context)



def registerPage(request):
    form = CreateUserForm()
    
    if request.method =="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('home')
    
    context = {'form':form}
    return render(request, 'tasks/register.html', context)


def loginPage(request):

    if request.method == 'POST':
        uname = request.POST.get('username')
        psw = request.POST.get('password')

        user = authenticate(request, username=uname, password=psw)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.info(request, 'Benutzername oder Passwort ist inkorrekt.')

    context = {}
    return render(request, 'tasks/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
