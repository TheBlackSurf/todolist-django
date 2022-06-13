from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Task
from .forms import TaskForm


def taskView(request):
    tasks = Task.objects.order_by("completed", "-created")
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-view')
        else:
            TaskForm()
    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'core/task-view.html', context)


def taskDelete(request, pk):
    tasks = Task.objects.get(pk=pk)
    if request.method == 'POST':
        tasks.delete()
        return redirect('task-view')
    context = {
        'tasks': tasks,
    }
    return render(request, 'core/task-delete.html', context)


def taskUpdate(request, pk):
    tasks = Task.objects.get(pk=pk)
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tasks)
        form.save()
        return redirect('task-view')
    else:
        form = TaskForm(instance=tasks)
    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'core/task-update.html', context)


def allremove(request):
    if request.method == 'POST':
        Task.objects.all().delete()
        return redirect('task-view')
    return render(request, 'core/all-remove.html')
