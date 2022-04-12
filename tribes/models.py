from django.conf import settings
from django.db.models import *

from customAuth.models import UserTribeMember


class Tribe(Model):
    chieftain = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    name = CharField(max_length=128, default="", unique=True)
    # TODO: figure out how to upload files
    # TODO: see https://wsofter.com/upload-download-file-to-from-server-in-django-via-ajax/
    # file = request.FILES.get('file')
    # File.objects.create(file=file)
    logo = FileField(upload_to='', null=True)
    genre = CharField(max_length=32, null=True, default="None")

    # todo rework these exceptions to use a base exception and have the message be passed per exception
    class ChieftainCannotLeavePleaseDisbandException(Exception):
        def __init__(self, user, tribe):
            super().__init__(
                f'{user} is the chieftain of {tribe} and can not leave {tribe}, please disband tribe instead.')

    class UserIsNotInTribeCannotLeaveException(Exception):
        def __init__(self, user, tribe):
            super().__init__(f'{user} is not a member of {tribe} and can not leave {tribe}.')

    class UserIsAlreadyAMemberException(Exception):
        def __init__(self, user, tribe):
            super().__init__(f'{user} is already a member of {tribe} and can not join again.')

    class TribeAlreadyExistsException(Exception):
        def __init__(self, name):
            super().__init__(f'A tribe with the name {name} already exists')

    class UserCannotCreatePlaylistException(Exception):
        def __init__(self, user, tribe):
            super().__init__(f'{user} is not the chieftain of {tribe} and can not create a playlist.')

    def getMembers(self):
        relation = UserTribeMember.objects.filter(tribe=self).all()
        users = []
        for i in relation:
            users.append(i.user)
        return users

    def createPlaylist(self, name, description):
        return Playlist.objects.create(tribe=self,
                                       user=self.chieftain,
                                       name=name,
                                       description=description)

    def addMember(self, user):
        membership = list(UserTribeMember.objects.filter(tribe=self, user=user).all())
        if len(membership) > 0:
            raise self.UserIsAlreadyAMemberException(user, self)
        UserTribeMember.objects.create(tribe=self, user=user)

    def __str__(self):
        return self.name


class Message(Model):
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    tribe = ForeignKey(Tribe, on_delete=CASCADE)
    content = CharField(max_length=128)
    date = DateTimeField(auto_now_add=True)


class Playlist(Model):
    tribe = ForeignKey(Tribe, on_delete=CASCADE)
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    name = CharField(max_length=128, default="")
    description = CharField(max_length=256, null=True, default="None")


class Song(Model):
    playlist = ForeignKey(Playlist, on_delete=CASCADE)
    link = URLField(max_length=256)
    title = CharField(max_length=128)
    artist = CharField(max_length=32, null=True)
    duration = IntegerField(null=True)


class UserLike(Model):
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    song = ForeignKey(Song, on_delete=CASCADE)


class UserComment(Model):
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    song = ForeignKey(Song, on_delete=CASCADE)
    content = CharField(max_length=512)
    date = DateTimeField(auto_now_add=True)
