from django.shortcuts import render, redirect
from .models import Task

def index(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('/')
    return render(request, 'teste/list.html', {'tasks': tasks})

def delete_task(request, task_id):
    Task.objects.filter(id=task_id).delete()
    return redirect('/')
