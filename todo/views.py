from django.shortcuts import render
from .models import Category, Task
from django.http import HttpResponseRedirect
from .forms import TaskUpdateForm, TaskCreateForm, CategoryCreateForm
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required()
def todolist(request):
	tasks = Task.objects.filter(author=request.user)
	categories = Category.objects.filter(author=request.user)
	form = TaskCreateForm(request.user)
	return render(request, 'todolist.html', {'tasks':tasks, 'categories': categories, 'form': form})


@login_required()
def delete(request, slug):
	task = Task.objects.get(slug=slug)
	task.delete()
	return HttpResponseRedirect('/')


@login_required()
def setattr(request, slug):
	task = Task.objects.get(slug=slug)
	task.completed = False if task.completed else True
	task.save()
	return HttpResponseRedirect('/')


@login_required()
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
@login_required()
def maketask(request):
	if request.method == 'POST':
		form = Task.objects.create(content=request.POST['content'], author=request.user)
		return HttpResponseRedirect('/')
	return HttpResponseRedirect('/')


@login_required()
def create(request):
	if request.method == 'POST':
		form = TaskCreateForm(request.user, request.POST)
		if form.is_valid():
			task = form.save(commit=False)
			task.author = request.user
			task.save()
		return HttpResponseRedirect('/')
	form = TaskCreateForm(request.user)
	return render(request, 'create_with_category.html', {'form': form})


@login_required()
def category(request, slug):
	category = Category.objects.get(slug=slug)
	return render(request, 'category.html', {'category': category})


@login_required()
def create_category(request):
	if request.method == 'POST':
		form = CategoryCreateForm(request.user, request.POST)
		if form.is_valid():
			category = form.save(commit=False)
			category.author = request.user
			category.save()
			return HttpResponseRedirect(reverse('todolist'))
	form = CategoryCreateForm(request.user)
	return render(request, 'create_category.html', {'form': form})


class SignUp(CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'registration/signup.html'