from django.urls import path, include

from tribes.views import *

app_name = 'tribes'
urlpatterns = [
    path('', index, name='index'),
]
