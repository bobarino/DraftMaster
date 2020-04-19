from sqlalchemy import Column, Date, Integer, String, Float
from sqlalchemy.orm import sessionmaker
import pandas as pd
from pybaseball import pitching_stats

from models.base import Base
from utils.constants import *
from utils.session import load_session

def fill_pitching_statistics(engine):
    session = load_session(engine)
    data = pitching_stats(PITCHING_START_YEAR, PITCHING_END_YEAR)
    print(data.columns)
    #TODO- Find what columns are important (there are 299)

class Pitching(Base):
    __tablename__ = MLB_PITCHING_TABLE

    #TODO- Change to a foreign key to player id
    PitchingID = Column(Integer, primary_key=True)

    #TODO- Fill out
    def __repr__(self):
        return "<Rankings>"
