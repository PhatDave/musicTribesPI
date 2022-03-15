from django.test import TestCase

from customauth.models import User
from tribes.models import *


class TribeTests(TestCase):
    def setUp(self):
        mirko = User.objects.create(username="mirko")
        bosko = User.objects.create(username="bosko")
        ivan = User.objects.create(username="ivan")
        cedo = User.objects.create(username="cedo")

        mirkoTribe = Tribe.objects.create(name="mirkovTribe", chieftain=mirko)
        boskoTribe = Tribe.objects.create(name="boskovTribe", chieftain=bosko)

        UserTribeMember.objects.create(user=mirko, tribe=boskoTribe)
        UserTribeMember.objects.create(user=ivan, tribe=boskoTribe)
        UserTribeMember.objects.create(user=cedo, tribe=boskoTribe)
        UserTribeMember.objects.create(user=ivan, tribe=mirkoTribe)
        UserTribeMember.objects.create(user=cedo, tribe=mirkoTribe)

        # TODO: ensure only chiefs can make playlists
        playlist1 = Playlist.objects.create(user=mirko, tribe=mirkoTribe)
        playlist2 = Playlist.objects.create(user=bosko, tribe=boskoTribe)

        song1 = Song.objects.create(playlist=playlist1, link="", title="song a")
        song2 = Song.objects.create(playlist=playlist1, link="", title="song b")
        song3 = Song.objects.create(playlist=playlist1, link="", title="song c")
        song4 = Song.objects.create(playlist=playlist2, link="", title="song d")

        UserLike.objects.create(user=ivan, song=song1)
        UserLike.objects.create(user=ivan, song=song2)
        UserLike.objects.create(user=ivan, song=song3)
        UserLike.objects.create(user=ivan, song=song4)
        UserLike.objects.create(user=cedo, song=song1)
        UserLike.objects.create(user=cedo, song=song2)
        UserLike.objects.create(user=cedo, song=song3)
        UserLike.objects.create(user=ivan, song=song1)

        UserComment.objects.create(user=ivan, content="ivan says hi", song=song1)
        UserComment.objects.create(user=bosko, content="bosko says hi", song=song1)
        UserComment.objects.create(user=cedo, content="cedo says hi", song=song1)
        UserComment.objects.create(user=ivan, content="ivan says hi!", song=song2)
        UserComment.objects.create(user=ivan, content="ivan says hi!!", song=song3)
        UserComment.objects.create(user=mirko, content="ivan says hi (but it was mirko all along)", song=song4)

        Message.objects.create(user=mirko, tribe=mirkoTribe, content="mirko thinks tribe is great")
        Message.objects.create(user=mirko, tribe=boskoTribe, content="mirko thinks tribe sucks")
        Message.objects.create(user=bosko, tribe=boskoTribe, content="bosko thinks...")
        Message.objects.create(user=ivan, tribe=mirkoTribe, content="wowiee")
        Message.objects.create(user=cedo, tribe=mirkoTribe, content="make tribe great again")

    def test_tribeGetMembers_returnsCorrectly(self):
        tribe = Tribe.objects.all()[0]
        ivan = User.objects.get(username="ivan")
        cedo = User.objects.get(username="cedo")
        self.assertEqual(tribe.getMembers(), [ivan, cedo])

    def test_tryJoinTribeOnValidUser(self):
        tribe = Tribe.objects.all()[0]
        bosko = User.objects.get(username="bosko")
        bosko.joinTribe(tribe)
    def test_tryJoinTribeUserIsAlreadyIn_throwsException(self):
        tribe = Tribe.objects.all()[0]
        ivan = User.objects.get(username="ivan")
        self.assertRaises(Tribe.UserIsAlreadyAMemberException, ivan.joinTribe, tribe=tribe)