from tribes.models import *


def createTribe(user, name="", logo="", genre="") -> Tribe:
    existingTribe = Tribe.objects.filter(name=name).all()
    if len(existingTribe) > 0:
        raise Tribe.TribeAlreadyExistsException(name)
    tribe = Tribe.objects.create(
        chieftain=user,
        name=name,
        logo=logo,
        genre=genre,
    )
    UserTribeMember.objects.create(user=user, tribe=tribe)
    return tribe
