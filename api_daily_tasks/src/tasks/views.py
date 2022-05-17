from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serializers import TaskSerializer
import django_filters.rest_framework

from .models import Task

#from django.utils.translation import ugettext as _

class ListTaskAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer
    #permission_classes = (permissions.IsAuthenticated, )
    queryset = Task.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['status',]

class CreateTaskAPIView(generics.CreateAPIView):
    serializer_class = TaskSerializer
    #permission_classes = (permissions.IsAuthenticated, )
    queryset = Task.objects.all()

class UpdateTaskAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = TaskSerializer
    #permission_classes = (permissions.IsAuthenticated, )
    queryset = Task.objects.all()

task = ListTaskAPIView.as_view()
task_create = CreateTaskAPIView.as_view()
task_update = UpdateTaskAPIView.as_view()