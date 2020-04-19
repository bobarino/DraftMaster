from sqlalchemy import Column, Date, Integer, String, Float
from sqlalchemy.orm import sessionmaker
import pandas as pd
from pybaseball import batting_stats_range
import progressbar

from models.base import Base
from utils.constants import *
from utils.session import load_session

def fill_batting_statistics(engine):
    session = load_session(engine)
    data = batting_stats_range(START_DATE, END_DATE)
    data.rename(columns={'2B':'Double',
                        '3B':'Triple'},
                        inplace=True)
    batting = [Batting(Name=d.Name, Age=d.Age, Date=d.Date, Team=d.Tm, Opponent=d.Opp, G=d.G,
                        PA=d.PA, AB=d.AB, R=d.R, H=d.H, Double=d.Double, Triple=d.Triple, HR=d.HR, RBI=d.RBI,
                        BB=d.BB, IBB=d.IBB, SO=d.SO, HBP=d.HBP, SH=d.SH, SF=d.SF, GDP=d.GDP, SB=d.SB,
                        CS=d.CS, BA=d.BA, OBP=d.OBP, SLG=d.SLG, OPS=d.OPS) for d in data.itertuples()]
    for b in batting:
        session.add(b)
        session.commit()

class Batting(Base):
    __tablename__ = MLB_BATTING_TABLE

    #TODO- Change to a foreign key to player id
    BattingID = Column(Integer, primary_key=True)
    Name = Column(String)
    Age = Column(Integer)
    Lev = Column(String)
    Date = Column(String)
    Team = Column(String)
    Opponent = Column(String)
    G = Column(String)
    PA = Column(String)
    AB = Column(String)
    R = Column(String)
    H = Column(String)
    Double = Column(String)
    Triple = Column(String)
    HR = Column(String)
    RBI = Column(String)
    BB = Column(String)
    IBB = Column(String)
    SO = Column(String)
    HBP = Column(String)
    SH = Column(String)
    SF = Column(String)
    GDP = Column(String)
    SB = Column(String)
    CS = Column(String)
    BA = Column(String)
    OBP = Column(String)
    SLG = Column(String)
    OPS = Column(String)

    #TODO- Fill out
    def __repr__(self):
        return "<Rankings>"
