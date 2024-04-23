from django.urls import path
from users.views import register_user_view, login_user_view, logout_user_view, dashboard_view

app_name='users'
urlpatterns = [
    path('', register_user_view, name='register_user'),
    path('login-user/', login_user_view, name='login_user'),
    path('logout-user/', logout_user_view, name='logout_user'),
    path('dashboard/', dashboard_view, name='dashboard')
]
