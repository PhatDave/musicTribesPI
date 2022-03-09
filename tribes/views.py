from django.shortcuts import render

from customauth.models import User
from tribes.models import *


def index(request):
    context = {}
    html = 'tribes/index.html'

    users = User.objects.all()
    for user in users:
        user.delete()
    tribes = Tribe.objects.all()
    for tribe in tribes:
        tribe.delete()

    user = User.objects.create(username="Dave")
    tribe = Tribe.objects.create(chieftain=user)

    return render(request, html, context)
