from django.urls import path
from .views import register, login_view, student_page, staff_page, error_page,admin_page, editor_page,logout_user

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('student_page/', student_page, name='student_page'),
    path('staff_page/', staff_page, name='staff_page'),
    path('admin_page/', admin_page, name='admin_page'),
    path('editor_page/', editor_page, name='editor_page'),
    path('error_page/', error_page, name='error_page'),

    path('logout/', logout_user, name='logout'),
]
