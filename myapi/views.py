from django.shortcuts import render
from .serializers import TaskSerializer
from rest_framework import viewsets
from .models import Task
# Create your views here.

class ApiViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by("title")
    serializer_class = TaskSerializer
