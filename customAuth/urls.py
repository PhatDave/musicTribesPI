from django.urls import path

from customAuth.views import loginView, registerView

app_name = 'auth'
urlpatterns = [
    path('login/', loginView, name='login'),
    path('register/', registerView, name='register'),
    path('logout/', loginView, name='logout'),
]
