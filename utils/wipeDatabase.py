import os
import postgresql

conn = None

try:
    import environmentConfig
    conn = postgresql.open(f'pq://{environmentConfig.POSTGRES_USER}:{environmentConfig.POSTGRES_PASSWORD}@{environmentConfig.POSTGRES_HOST}:{environmentConfig.POSTGRES_PORT}/{environmentConfig.POSTGRES_NAME}')
except ModuleNotFoundError:
    conn = postgresql.open(f'pq://{os.environ.get("POSTGRES_USER")}:{os.environ.get("POSTGRES_PASSWORD")}@{os.environ.get("POSTGRES_HOST")}:{os.environ.get("POSTGRES_PORT")}/{os.environ.get("POSTGRES_NAME")}')

conn.execute("DROP SCHEMA public CASCADE;")
conn.execute("CREATE SCHEMA public;")

os.system("py utils/cleanMigrations.py")
os.system("py manage.py makemigrations")
os.system("py manage.py migrate")
os.system("py utils/dataGenerator.py")