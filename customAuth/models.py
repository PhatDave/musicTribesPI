from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models import *

from tribes.models import *


class User(AbstractUser):
    pass

class UserTribeMember(Model):
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    tribe = ForeignKey(Tribe, on_delete=CASCADE)