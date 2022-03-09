from django.conf import settings
from django.db.models import *

from customauth.models import UserTribeMember


class Tribe(Model):
    chieftain = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    name = CharField(max_length=128, default="")
    # TODO: use server hosted media for this
    # logo = URLField
    genre = CharField(max_length=32, null=True, default=None)

    def getMembers(self):
        return UserTribeMember.objects.filter(tribe=self).all()

class Message(Model):
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    tribe = ForeignKey(Tribe, on_delete=CASCADE)
    content = CharField(max_length=128)
    date = DateTimeField(auto_now_add=True)


class Playlist(Model):
    tribe = ForeignKey(Tribe, on_delete=CASCADE)
    owner = ForeignKey(settings.AUTH_USER_MODEL, on_delete=SET_DEFAULT, default="None", null=True)
    name = CharField(max_length=128, default="")
    description = CharField(max_length=256, null=True, default=None)

class Song(Model):
    playlist = ForeignKey(Playlist, on_delete=CASCADE)
    link = URLField(max_length=256)
    title = CharField(max_length=128)
    artist = CharField(max_length=32)
    duration = IntegerField()

class UserLike(Model):
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    song = ForeignKey(Song, on_delete=CASCADE)

class UserComment(Model):
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    song = ForeignKey(Song, on_delete=CASCADE)
    content = CharField(max_length=512)
    date = DateTimeField(auto_now_add=True)