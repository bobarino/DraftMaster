from sqlalchemy import Column, Date, Integer, String, Float
from sqlalchemy.orm import sessionmaker
import pandas as pd
from pybaseball import standings
import progressbar

from models.base import Base
from utils.constants import *
from utils.session import load_session

def fill_rankings(engine):
    session = load_session(engine)
    standings_list = standings()
    for data in standings_list:
        data.rename(columns={'W-L%':'WLPercent'}, inplace=True)
        rankings = [Rankings(Team=d.Tm, Win=d.W, Loss=d.L, WLPercent=d.WLPercent, GB=d.GB) for d in data.itertuples()]
        for r in rankings:
            session.add(r)
            session.commit()

class Rankings(Base):
    __tablename__ = MLB_RANKINGS_TABLE

    RankingId = Column(Integer, primary_key=True)
    Team = Column(String)
    Win = Column(Integer)
    Loss = Column(Integer)
    WLPercent = Column(String)
    GB = Column(String)

    #TODO- Fill out
    def __repr__(self):
        return "<Rankings>"
