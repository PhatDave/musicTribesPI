from django.conf import settings
from django.db.models import *


class Tribe(Model):
    chieftain = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    name = CharField(max_length=128, default="")
    # TODO: use server hosted media for this
    # logo = URLField
    genre = CharField(max_length=32, null=True, default=None)


class Playlist(Model):
    tribe = ForeignKey(Tribe, on_delete=CASCADE)
    owner = ForeignKey(settings.AUTH_USER_MODEL, on_delete=SET_DEFAULT, default="None", null=True)
    name = CharField(max_length=128, default="")
    description = CharField(max_length=256, null=True, default=None)
