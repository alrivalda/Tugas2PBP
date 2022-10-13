from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import create_Task
from django.core import serializers
# Create your views here.cd
@login_required(login_url="/todolist/login")
def show_index(request): 
    task = Task.objects.filter(user = request.user)
    context = {
        "list_task" : task,
    }
    return render (request,'todolist.html', context)

@login_required(login_url="/todolist/login")
def create_task (request) :
    if request.method == "POST":
        task_form = create_Task(request.POST)
        if task_form.is_valid():
            createtask = task_form.save(commit=False)
            createtask.user = request.user
            messages.success(request, "Task succesfully created")
            createtask.save()
            return redirect("todolist:show_index")
    else:
        task_form = create_Task()
    context = {
        "task" : task_form
    }   
    return render(request,"createtask.html",context)

@login_required(login_url="/todolist/login")
def update_task(request ,pk):
    task = Task.objects.get(pk=pk)
    task.finished = not task.finished
    task.save()
    messages.success(request,"Succcesfully update")
    return redirect("todolist:show_index")

@login_required(login_url="/todolist/login")
def delete_task(request ,pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    messages.success(request,"Succcesfully delete")
    return redirect("todolist:show_index")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('todolist:show_index')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect("todolist:login")


#T6
def show_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def create_task_ajax(request):
    if request.method == "POST":
        title = request.POST.get('tittle')
        description = request.POST.get('description')
        todo = Task.objects.create(
            user=request.user,
            title=title, 
            description=description,
            date=datetime.now(), 
            finished=False
        )
        context = {
            'pk':todo.pk,
            'fields':{
                'title':todo.title,
                'description':todo.description,
                'is_finished':todo.is_finished,
                'date':todo.date,
            }
        }
        return JsonResponse(context)