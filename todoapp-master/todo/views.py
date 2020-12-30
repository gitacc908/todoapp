from django.shortcuts import render
from .models import Category, Task
from django.http import HttpResponseRedirect
from .forms import TaskUpdateForm, TaskCreateForm, CategoryCreateForm
from django.urls import reverse
# Create your views here.

def todolist(request):
	tasks = Task.objects.all()
	categories = Category.objects.all()
	form = TaskCreateForm()
	return render(request, 'todolist.html', {'tasks':tasks, 'categories': categories, 'form': form})


def delete(request, slug):
	task = Task.objects.get(slug=slug)
	task.delete()
	return HttpResponseRedirect('/')


def setattr(request, slug):
	task = Task.objects.get(slug=slug)
	task.completed = False if task.completed else True
	task.save()
	return HttpResponseRedirect('/')


def update(request, slug):
	task = Task.objects.get(slug=slug)
	form = TaskUpdateForm(instance=task)
	if request.method == 'POST':
		form = TaskUpdateForm(request.POST, instance=task)
		if form.is_valid():
			updated_task = form.save()
			return HttpResponseRedirect('/')
	return render(request, 'update.html', {'form': form, 'task': task})


# Here we creating task with default None category 
def maketask(request):
	if request.method == 'POST':
		form = Task.objects.create(content=request.POST['content'])
		return HttpResponseRedirect('/')
	return HttpResponseRedirect('/')

def create(request):
	if request.method == 'POST':
		form = TaskCreateForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/')
	form = TaskCreateForm()
	return render(request, 'create_with_category.html', {'form': form})


def category(request, slug):
	category = Category.objects.get(slug=slug)
	return render(request, 'category.html', {'category': category})

def create_category(request):
	if request.method == 'POST':
		form = CategoryCreateForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('todolist'))
	form = CategoryCreateForm()
	return render(request, 'create_category.html', {'form': form})