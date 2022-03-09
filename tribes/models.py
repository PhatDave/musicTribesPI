from django.conf import settings
from django.db.models import *

from customauth.models import UserTribeMember


class Tribe(Model):
    chieftain = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    name = CharField(max_length=128, default="")
    # TODO: figure out how to upload files
    # TODO: see https://wsofter.com/upload-download-file-to-from-server-in-django-via-ajax/
    # file = request.FILES.get('file')
    # File.objects.create(file=file)
    logo = FileField(upload_to='', null=True)
    genre = CharField(max_length=32, null=True, default=None)

    def getMembers(self):
        relation = UserTribeMember.objects.filter(tribe=self).all()
        users = []
        for i in relation:
            users.append(i.user)
        return users

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