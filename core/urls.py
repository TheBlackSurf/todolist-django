from django.urls import path
from . import views
urlpatterns = [
    path('', views.taskView, name='task-view'),
    path('task-delete/<int:pk>', views.taskDelete, name='task-delete'),
    path('task-update/<int:pk>', views.taskUpdate, name='task-update'),
    path('all-remove/', views.allremove, name='all-remove'),
]
