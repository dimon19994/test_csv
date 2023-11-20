from peewee import TextField, DateField

from models import _Model


class Data(_Model):
    class Meta:
        db_table = "data"

    category = TextField()
    first_name = TextField()
    last_name = TextField()
    email = TextField()
    gender = TextField()
    birth_date = DateField()
