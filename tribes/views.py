from django.shortcuts import render

from customAuth.models import User
from tribes.models import *


def index(request):
    html = 'tribes/index.html'
    tribe = Tribe.objects.all()[0]
    print(tribe.getMembers())
    context = {
        'nav': 'index',
    }
    return render(request, html, context)
