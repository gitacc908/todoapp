from django.db import models
from autoslug import AutoSlugField


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='category')
    slug = AutoSlugField(populate_from='name', unique=True)
    parent = models.ForeignKey('self',on_delete=models.CASCADE, blank=True, null=True , related_name='children', verbose_name='category_parent')

    class Meta:
        #enforcing that there can not be two categories under a parent with same slug
        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"     

    def __str__(self):                           
        full_path = [self.name]                  
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])


class Task(models.Model):
	category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='task', null=True, blank=True)
	content = models.CharField(max_length=350, unique=True)
	completed = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	slug = AutoSlugField(unique=True, populate_from='content')

	def __str__(self):
		return self.content