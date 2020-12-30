from django import forms
from .models import Task, Category

class TaskCreateForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['category','content']

		

class TaskUpdateForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['category', 'content']

class CategoryCreateForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['parent', 'name']