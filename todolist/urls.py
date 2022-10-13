from django.urls import path
from todolist.views import  login_user ,register, show_index, create_task, logout_user,update_task,delete_task,show_json,create_task_ajax


# menambah path dan meminta request pada view
app_name ='todolist'
urlpatterns = [
    path('', show_index, name='show_index'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('create-task/', create_task, name='create_task'),
    path('logout/', logout_user, name='logout'),
    path('update-task/<int:pk>', update_task, name='update'),
    path('delete-task/<int:pk>', delete_task, name='delete'),
    path('json/', show_json, name='show-json'),
    path('add/', create_task_ajax, name='create-task-ajax')

]