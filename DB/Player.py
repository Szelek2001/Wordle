from sqlalchemy import Column, create_engine
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

# Dane połączenia

engine = create_engine('mysql+pymysql://root:2137@127.0.0.1:3306/player')
Base = declarative_base()


class Player(Base):
    # tworzenie tabeli do Databazy
    __tablename__ = "player"
    player_name = Column('playername', String(255), primary_key=True)
    password = Column('password', String(255))
    game = Column('game', Integer)
    win = Column('win', Integer)
    lose = Column('lose', Integer)
    A1 = Column('a1', Integer)
    A2 = Column('a2', Integer)
    A3 = Column('a3', Integer)
    A4 = Column('a4', Integer)
    A5 = Column('a5', Integer)
    A6 = Column('a6', Integer)

    def __init__(self, login, password):
        self.player_name = login
        self.password = password
        self.game = 0
        self.win = 0
        self.lose = 0
        self.A1 = 0
        self.A2 = 0
        self.A3 = 0
        self.A4 = 0
        self.A5 = 0
        self.A6 = 0


Base.metadata.create_all(bind=engine)
