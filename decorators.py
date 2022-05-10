from functools import wraps

from tribes.models import Tribe


# todo make this work later...
def requireChieftain(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        user = request.user
        if user.isChieftain:
            return func(request, *args, **kwargs)
        else:
            return Tribe.UserCannotCreatePlaylistException(request.user)
    return wrapper