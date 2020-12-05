from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo

# The viewsets base class provides the implementation for CRUD operations by default, 
# what we had to do was specify the serializer class and the query set.
class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
