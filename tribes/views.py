from django.shortcuts import render

from customAuth.models import User
from tribes.models import *


def index(request):
    context = {}
    html = 'tribes/index.html'

    tribes = Tribe.objects.all()
    context['tribes'] = tribes

    return render(request, html, context)
