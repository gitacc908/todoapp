from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.todolist, name='todolist'),
    path('create/', views.create, name='create'),
    path('maketask/', views.maketask, name='maketask'),
    path('create_category/', views.create_category, name='create_category'),
    path('delete/<str:slug>/', views.delete, name='delete'),
    path('setattr/<str:slug>/', views.setattr, name='setattr'),
    path('update/<str:slug>/', views.update, name='update'),
    path('category/<str:slug>/', views.category, name='category'),
]
