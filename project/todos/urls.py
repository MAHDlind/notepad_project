from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.todo_dashboard, name='dashboard'),
    path('create/', views.create_todo, name='create'),
    path('toggle/<int:todo_id>/', views.toggle_todo_status, name='toggle'),
    path('add/', views.add_todo_item, name='add_todo_item'),
]
