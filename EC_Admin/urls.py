from django.urls import path
from . import views

urlpatterns = [
    path('adminhome', views.adminhome, name='adminhome'),
    path('adminprofile', views.adminprofile, name='adminprofile'),
    path('addproject', views.addproject, name='addproject'),
    path('add_project', views.add_project, name='add_project'),
    path('addaffiliate', views.addaffiliate, name='addaffiliate'),
    path('add_affiliate', views.add_affiliate, name='add_affiliate'),
    path('view_affiliate', views.view_affiliate, name='view_affiliate'),
    path('viewproject', views.viewproject, name='viewproject'),
    path('view_project', views.view_project, name='view_project'),
    path('editproject', views.editproject, name='editproject'),
    path('edit_project', views.edit_project, name='edit_project'),
    path('editprojectdetails', views.editprojectdetails, name='editprojectdetails'),
    path('todo_list', views.todo_list, name='todo_list'),
    path('add_task', views.add_task, name='add_task'),
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
    path('mark_done/<int:pk>/', views.mark_done, name='mark_done'),
    path('not_ready', views.not_ready, name='not_ready'),
]
