from django.urls import path
from .views import CustomLoginVeiw, LogoutView, CustomRegister
app_name ='users'
urlpatterns = [
    path('user-register/', CustomRegister.as_view(), name= 'register' ),
    path('user-login/', CustomLoginVeiw.as_view(), name= 'login' ),
    path('user-logout/',LogoutView.as_view(next_page = 'todo:tasks'), name= 'logout' ),
    # path('', Tasklist.as_view(), name= 'tasks' ),
    # path('task/<str:pk>/', TaskDetail.as_view(), name= 'task' ),
    # path('task-create/', TaskCreate.as_view(), name= 'task-create' ),
    # path('task-update/<str:pk>/', TaskUpdate.as_view(), name= 'task-update' ),
    # path('task-delete/<str:pk>/', TaskDelete.as_view(), name= 'task-delete' ),
]  