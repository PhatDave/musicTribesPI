from django.contrib.auth.models import AbstractUser
from django.db.models import *

from tribes.models import *


class User(AbstractUser):
    pass

class UserTribeMember(Model):
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    tribe = ForeignKey("tribes.Tribe", on_delete=CASCADE)