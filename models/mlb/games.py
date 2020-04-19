from sqlalchemy import Column, Date, Integer, String, Float
from sqlalchemy.orm import sessionmaker
import pandas as pd
from pybaseball import schedule_and_record

from models.base import Base
from utils.constants import *
from utils.session import load_session

def fill_game_statistics(engine):
    session = load_session(engine)
    for team in MLB_TEAMS_PYBASEBALL:
        data = schedule_and_record(2018, team)
        data.rename(columns={'W-L':'WL',
                            'W/L':'WLRecord',
                            'D/N':'DN',
                            'Orig. Scheduled':'OrigScheduled'},
                            inplace=True)
        games = [Games(Date=d.Date, Team=d.Tm, HomeAway=d.Home_Away, Opponent=d.Opp, WL=d.WL, R=d.R, RA=d.RA, Inn=d.Inn,
                        WLRecord=d.WLRecord, Rank=d.Rank, GB=d.GB, Win=d.Win, Loss=d.Loss, Save=d.Save, Time=d.Time,
                        DN=d.DN, Attendance=d.Attendance, Streak=d.Streak, OrigScheduled=d.OrigScheduled) for d in data.itertuples()]
        for g in games:
            session.add(g)
            session.commit()

class Games(Base):
    __tablename__ = MLB_GAMES_TABLE

    GameId = Column(Integer, primary_key=True)
    Date = Column(String)
    Team = Column(String)
    HomeAway = Column(String)
    Opponent = Column(String)
    WL = Column(Integer)
    R = Column(Float)
    RA = Column(Float)
    Inn = Column(Integer)
    WLRecord = Column(String)
    Rank = Column(Integer)
    GB = Column(String)
    Win = Column(String)
    Loss = Column(String)
    Save = Column(String)
    Time = Column(String)
    DN = Column(String)
    Attendance = Column(Float)
    Streak = Column(Integer)
    OrigScheduled = Column(String)

    #TODO- Pretty Print
    def __repr__(self):
        return "<Games(GameId='%d', Date='%s', Team='%s', HomeAway='%s', Opponent='%s', WL='%d', R='%d', RA='%d', Inn='%d', WLRecord='%s', Rank='%d', GB='%s', Win='%s', Loss='%s', Save='%s', Time='%s', DN='%s', Attendance='%d', Streak='%d', OrigScheduled='%s')>"% (self.GameId,
                self.Date, self.Team, self.HomeAway, self.Opponent, self.WL, self.R, self.RA, self.Inn, self.WLRecord, self.Rank, self.GB, self.Win, self.Loss, self.Save, self.Time, self.DN, self.Attendance, self.Streak, self.OrigScheduled)
