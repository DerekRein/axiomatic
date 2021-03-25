from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DECIMAL, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()


"""
Using a SqAlchemy to persist trading data rather than keep it in memory.
"""


class Bars(Base):

    __tablename__ = 'bars'

    id = Column(Integer, primary_key=True)
    contract = ForeignKey(Integer, primary_key=True)
    size = Column(Integer)
    time = Column(DateTime)
    open = Column(DECIMAL)
    high = Column(DECIMAL)
    low = Column(DECIMAL)
    close = Column(DECIMAL)
    volume = Column(DECIMAL)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname)


class Trades(Base):

    __tablename__ = 'trades'

    id = Column(Integer, primary_key=True)
    contract = ForeignKey(Integer, primary_key=True)
    size = Column(Integer)
    time = Column(DateTime)
    open = Column(DECIMAL)
    high = Column(DECIMAL)
    low = Column(DECIMAL)
    close = Column(DECIMAL)
    volume = Column(DECIMAL)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname)



Session = sessionmaker(bind=engine)