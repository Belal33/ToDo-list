from django.urls import path
from .views import TaskDelete, Tasklist ,TaskDetail, TaskCreate ,TaskUpdate #,CustomLoginVeiw,LogoutView,CustomRegister
app_name ='todo'
urlpatterns = [
    path('', Tasklist.as_view(), name= 'tasks' ),
    path('task/<str:pk>/', TaskDetail.as_view(), name= 'task' ),
    path('task-create/', TaskCreate.as_view(), name= 'task-create' ),
    path('task-update/<str:pk>/', TaskUpdate.as_view(), name= 'task-update' ),
    path('task-delete/<str:pk>/', TaskDelete.as_view(), name= 'task-delete' ),
]  