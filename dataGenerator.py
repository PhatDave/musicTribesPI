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
db.setTable(user)

user.addColumns([
    Column("id", SerialGenerator(1), True),
    Column("username", FakeUsernameGenerator()),
    Column("password", RandomStringGenerator(16, True, True, True)),
    Column("first_name", FakeFirstNameGenerator()),
    Column("last_name", FakeLastNameGenerator()),
    Column("is_superuser", ConstantGenerator(False)),
    Column("is_staff", ConstantGenerator(False)),
    Column("is_active", ConstantGenerator(True)),
    Column("date_joined", FakeCurrentMonthDateTimeGenerator()),
])

db.insertRows(user, 200)