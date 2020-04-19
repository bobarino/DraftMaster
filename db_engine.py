from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import relationship, backref, sessionmaker
import models.base as base


class DBEngine():
    def __init__(self, db_name: str, leagues: list):
        self.engine = create_engine('sqlite:///' + db_name)
        self.leagues = leagues

    def create_tables(self):
        base.Base.metadata.create_all(self.engine, checkfirst=True)

    def fill_tables(self):
        for l in self.leagues:
            l.fill_table(self.engine)
