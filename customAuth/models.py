from django.contrib.auth.models import AbstractUser
from django.db.models import *

from tribes.models import *

class User(AbstractUser):
    def joinTribe(self, tribe):
        tribe.addMember(self)

    # TODO: implement and test
    def leaveTribe(self, tribe):
        pass

    def getUserTribes(self):
        pass

    def isInTribe(self, tribe):
        pass

class UserTribeMember(Model):
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    tribe = ForeignKey("tribes.Tribe", on_delete=CASCADE)