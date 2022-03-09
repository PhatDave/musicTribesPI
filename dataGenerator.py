import os

from DataGenerator import *
from DataGenerator.Generators import *
from DataGenerator.Table import *
from DataGenerator.Column import *

db = Databases.PostgreSQLDB(override=True)
try:
    import environmentConfig
    db.connect(user=environmentConfig.POSTGRES_USER,
               password=environmentConfig.POSTGRES_PASSWORD,
               ip=environmentConfig.POSTGRES_HOST,
               port=environmentConfig.POSTGRES_PORT,
               dbName=environmentConfig.POSTGRES_NAME)
except ModuleNotFoundError:
    db.connect(user=os.environ.get('POSTGRES_USER'),
               password=os.environ.get('POSTGRES_PASSWORD'),
               ip=os.environ.get('POSTGRES_HOST'),
               port=os.environ.get('POSTGRES_HOST'),
               dbName=os.environ.get('POSTGRES_NAME'))


user = Table("customAuth_user")
user.addColumns([
    Column("id", SerialGenerator(1), True),
    Column("username", FakeUsernameGenerator()),
    Column("password", RandomStringGenerator(16, True, True, True)),
    Column("email", FakeEmailGenerator()),
    Column("first_name", FakeFirstNameGenerator()),
    Column("last_name", FakeLastNameGenerator()),
    Column("is_superuser", ConstantGenerator(False)),
    Column("is_staff", ConstantGenerator(False)),
    Column("is_active", ConstantGenerator(True)),
    Column("date_joined", FakeCurrentMonthDateTimeGenerator()),
])

try:
    db.insertRows(user, 50)
except Exception as e:
    print(e)

tribe = Table("tribes_tribe")
tribe.addColumns([
    Column("id", SerialGenerator(1), True),
    Column("name", FakeUsernameGenerator()),
    Column("genre", FakeUsernameGenerator()),
    Column("chieftain_id", SetGenerator(db.getPkSet(user), True)),
])

try:
    db.insertRows(tribe, 50)
except Exception as e:
    print(e)

playlist = Table("tribes_playlist")
playlist.addColumns([
    Column("id", SerialGenerator(1), True),
    Column("name", FakeUsernameGenerator()),
    Column("description", FakeUsernameGenerator()),
    Column("owner_id", SetGenerator(db.getPkSet(user), True)),
    Column("tribe_id", SetGenerator(db.getPkSet(tribe), True)),
])

try:
    db.insertRows(playlist, 50)
except Exception as e:
    print(e)

song = Table("tribes_song")
song.addColumns([
    Column("id", SerialGenerator(1), True),
    Column("title", FakeUsernameGenerator()),
    Column("link", FakeUrlGenerator()),
    Column("artist", FakeUsernameGenerator()),
    Column("duration", RandomIntegerGenerator(0, 1e5)),
    Column("playlist_id", SetGenerator(db.getPkSet(playlist), True)),
])

try:
    db.insertRows(song, 50)
except Exception as e:
    print(e)

tribeMessage = Table("tribes_message")
tribeMessage.addColumns([
    Column("id", SerialGenerator(1), True),
    Column("content", RandomStringGenerator(128)),
    Column("date", FakeCurrentMonthDateTimeGenerator()),
    Column("tribe_id", SetGenerator(db.getPkSet(tribe), False)),
    Column("user_id", SetGenerator(db.getPkSet(user), False)),
])

try:
    db.insertRows(tribeMessage, 5000)
except Exception as e:
    print(e)

songComment = Table("tribes_usercomment")
songComment.addColumns([
    Column("id", SerialGenerator(1), True),
    Column("content", RandomStringGenerator(512)),
    Column("date", FakeCurrentMonthDateTimeGenerator()),
    Column("song_id", SetGenerator(db.getPkSet(song), False)),
    Column("user_id", SetGenerator(db.getPkSet(user), False)),
])

try:
    db.insertRows(songComment, 5000)
except Exception as e:
    print(e)

userLike = Table("tribes_userlike")
userLike.addColumns([
    Column("id", SerialGenerator(1), True),
    Column("song_id", SetGenerator(db.getPkSet(song), True)),
    Column("user_id", SetGenerator(db.getPkSet(user), True)),
])

try:
    db.insertRows(userLike, 5000)
except Exception as e:
    print(e)