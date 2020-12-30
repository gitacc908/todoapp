from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TaskSerializer, CategorySerializer
from todo.models import Task, Category
from todo.forms import TaskUpdateForm, TaskCreateForm, CategoryCreateForm

from rest_framework.decorators import api_view

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'task-list/' : '/',
        'update/<str:slug>/': 'update/<str:slug>/',
        'task-create/' : 'create/',
        'task-delete/<str:slug>/' : 'delete/<str:slug>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, slug):
    task = Task.objects.get(slug=slug)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, slug):
    task = Task.objects.get(slug=slug)
    task.delete()
    return Response("Taks deleted successfully.")