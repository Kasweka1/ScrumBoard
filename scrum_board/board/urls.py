from django.urls import path
from .views import ( user_dashboard, assign_task, 
                    all_users_tasks, CustomLoginView, CustomLogoutView,
                    register_user, edit_task, delete_task, transition_task)

urlpatterns = [
    path('dashboard/', user_dashboard, name='user_dashboard'),
    path('assign/', assign_task, name='assign_task'),
    path('all_users_tasks/', all_users_tasks, name='all_users_tasks'),
    path('register/', register_user, name='register_user'),
    path('edit_task/<int:task_id>/', edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('transition_task/<int:task_id>/<str:target_status>/', transition_task, name='transition_task'),
    # path('', loginPage, name='login_page'),

    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]