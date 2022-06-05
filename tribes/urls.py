from django.urls import path

from tribes.views import (
    index_view,
)

app_name = 'tribes'

urlpatterns = [
    path('', index_view, name='index'),
]
