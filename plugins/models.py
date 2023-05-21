from peewee import SqliteDatabase, Model, BigIntegerField, DateTimeField

# Create a database instance
db = SqliteDatabase('db.sqlite3')

# Sample model
class User(Model):
    user_id = BigIntegerField()
    name = CharField(dafult="Your User")

    class Meta:
        database = db

# Create tables if they don't exist
with db:
    db.create_tables([User])
