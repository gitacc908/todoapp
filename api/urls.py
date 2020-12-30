from django.urls import path
from .views import apiOverview, taskList, taskUpdate, taskCreate, taskDelete



app_name = "api"


# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('', apiOverview, name='api_overview'),
    path('task-list/', taskList, name="task-list"),
    path('update/<str:slug>/', taskUpdate, name='taskUpdate'),
    path('task-create/', taskCreate, name="task-create"),
    path('task-delete/<str:slug>/', taskDelete, name="task-delete"),
]