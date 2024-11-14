from django.urls import path
from . import views

urlpatterns = [
    path('', views.createTodoListView, name='todo_url'),
    path('show/', views.showTodoListView, name='show_url'),
    path('up/<int:f_id>', views.updateTodoListView, name= 'update_url'),
    path('del/<int:f_id>', views.deleteTodoListView, name= 'delete_url'),
]