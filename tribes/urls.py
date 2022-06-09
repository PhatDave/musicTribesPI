from django.urls import path
from tribes.views import (
    index_view,
    tribes_index_view,
    tribe_membership_view,
)

app_name = 'tribes'

urlpatterns = [
    path('', index_view, name='index'),
    path(f'{app_name}', tribes_index_view, name='tribes_index'),
    path(f'{app_name}/tribeMembership', tribe_membership_view, name='tribe_membership'),
]
