from django.shortcuts import render
from .serializers import TodoSerializer
from rest_framework import viewsets
from .models import Todo


class TodoView(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('completed', '-created_on')
    serializer_class = TodoSerializer


def index(request):
    return render(request, 'index.html')
