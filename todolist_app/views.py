from django.shortcuts import render, redirect
from .models import TaskList
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.manager = request.user
            new_task.save()
            messages.success(request, "Task added successfully")
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.filter(manager=request.user)
        paginator = Paginator(all_tasks, 5)
        page_number = request.GET.get('page')
        tasks_page = paginator.get_page(page_number)
        return render(request, 'todolist.html', {'tasks': tasks_page, 'paginator': paginator})

def contact(request):
    context = {
        'welcome_text': 'Welcome to Contact Us',
    }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        'welcome_text': 'Welcome to About',
    }
    return render(request, 'about.html', context)
    
@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if request.user != task.manager:
        messages.error(request, "You are not authorized to delete this task.")
        return redirect('todolist')
    task.delete()
    return redirect('todolist')
@login_required
def edit_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully")
        return redirect('todolist') 
    else:
        return render(request, 'edit.html', {'task': task})
@login_required
def toggle_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if request.user != task.manager:
        messages.error(request, "You are not authorized to toggle this task.")
        return redirect('todolist')
    task.done = not task.done
    task.save()
    messages.success(request, "Task status updated successfully")
    referer_url = request.META.get('HTTP_REFERER')
    return HttpResponseRedirect(referer_url)

def home(request):
    return render(request, 'home.html')