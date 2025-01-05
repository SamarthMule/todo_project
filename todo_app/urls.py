from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/add/', views.add_task, name='add_task'),
    path('tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('tasks/<int:task_id>/toggle/', views.toggle_task, name='toggle_task'), 
    path('task/edit/<int:task_id>/', views.edit_task, name='edit_task'),
]
