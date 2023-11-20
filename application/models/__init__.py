from peewee import Model, datetime as peewee_datetime
from playhouse.postgres_ext import PostgresqlExtDatabase

from config import DB_CONFIG

peewee_now = peewee_datetime.datetime.now

db = PostgresqlExtDatabase(**DB_CONFIG)
db.commit_select = True
db.autorollback = True


class _Model(Model):
    class Meta:
        database = db

    def __repr__(self):
        return "{class_name}(id={id})".format(
            class_name=self.__class__.__name__, id=self.id
        )

    @classmethod
    def get_by_id(cls, id):
        try:
            return cls.get(cls.id == id)
        except cls.DoesNotExist:
            return None
