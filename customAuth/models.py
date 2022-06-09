from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models import *


class User(AbstractUser):
	def joinTribe(self, tribe):
		tribe.addMember(self)

	def leaveTribe(self, tribe):
		# TODO: causes circular import because of UserTribeMember; I think this is fine
		from tribes.models import Tribe

		if self.isInTribe(tribe):
			if tribe.chieftain == self:
				raise Tribe.ChieftainCannotLeavePleaseDisbandException(self, tribe)
			UserTribeMember.objects.filter(user=self, tribe=tribe).get().delete()
		else:
			raise Tribe.UserIsNotInTribeCannotLeaveException(self, tribe)

	def getUserTribes(self):
		memberships = list(UserTribeMember.objects.filter(user=self).all())
		tribes = []
		for membership in memberships:
			tribes.append(membership.tribe)
		return tribes

	def isInTribe(self, tribe):
		membership = UserTribeMember.objects.filter(user=self, tribe=tribe)
		if len(membership) > 0:
			return True
		return False
		
	def serialize(self):
		return {
			'id': self.id,
			'first_name': self.first_name,
			'last_name': self.last_name,
			'email': self.email,
			'username': self.username,
		}


class UserTribeMember(Model):
	user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
	tribe = ForeignKey("tribes.Tribe", on_delete=CASCADE)
