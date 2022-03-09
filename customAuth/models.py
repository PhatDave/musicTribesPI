from django.contrib.auth.models import AbstractUser
from django.db.models import *


class User(AbstractUser):
    isMemberOf = ForeignKey("tribes.Tribe", on_delete=CASCADE, null=True)
