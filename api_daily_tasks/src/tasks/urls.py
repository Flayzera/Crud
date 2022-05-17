from django.urls import path
from .views import task, task_create, task_update

urlpatterns = [
    path('list/', task, name='tasks'),
    path('create/', task_create, name='task-create'),
    path('update/<int:pk>/', task_update, name='task-update'),
]