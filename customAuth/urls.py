from django.urls import path
from .views import (
	login_view,
    logout_view,
    register_view,
)

app_name = 'user'

urlpatterns = [
    path(f'{app_name}/login', login_view, name='login'),
	path('logout', logout_view, name='logout'),
    path(f'{app_name}/register', register_view, name='register'),
]