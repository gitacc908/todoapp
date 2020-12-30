from django import forms
from .models import Task, Category



class TaskCreateForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['category','content']

	def __init__(self, user, *args, **kwargs):
		super(TaskCreateForm, self).__init__(*args, **kwargs)
		self.fields['category'].queryset = Category.objects.filter(author=user)


class TaskUpdateForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['category', 'content']

class CategoryCreateForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['parent', 'name']

	def __init__(self, user, *args, **kwargs):
		super(CategoryCreateForm, self).__init__(*args, **kwargs)
		self.fields['parent'].queryset = Category.objects.filter(author=user)