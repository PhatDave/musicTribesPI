from django.urls import path
from .views import (
	login_view,
    logout_view,
)

app_name = 'user'

urlpatterns = [
    path(f'{app_name}/login', login_view, name='login'),
	path('logout', logout_view, name='logout'),
]