from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy_utils import database_exists, create_database

Base = declarative_base()

class Band(Base):
    __tablename__ = 'band'

    band_id = Column("band_id", Integer, primary_key=True)
    specialization = Column("specialization", String)
    level = Column("level", Integer)
    status = Column("status", String)
    nickname = Column("nickname", String)
    contact = Column("contact", String)
    date = Column("date", Date)

    robbery = relationship('Robbery', back_populates='Band')

class Robbery(Base):
    __tablename__ = "robbery"

    robbery_id = Column("robbery_id", Integer, primary_key=True)
    total_sum_for_each = Column("sum", Integer)
    part = Column("part", Integer)
    date = Column("date", Date)
    mark = Column("mark", Integer)

    band_id = Column(Integer, ForeignKey('band.band_id'), nullable=False)
    band = relationship('Band', back_populates='Robbery')
    bank = relationship('Bank', back_populates='Robbery')

class Bank(Base):
    __tablename__ = "bank"

    bank_id = Column("bank_id", Integer, primary_key=True)
    rate = Column("rate", Integer)
    total_sum = Column("total_sum", Integer)
    addres = Column("addres", String)
    security_rate = Column("security_rate", Integer)
    name = Column("name", String)

    robbery = relationship('Robbery', back_populates='Bank')


def initialize_db():
    DATABASE_URL = f'postgresql://arusyak:pass123@localhost:5432/my_project'
    engine = create_engine(DATABASE_URL)

    Base.metadata.create_all(engine)

if __name__ == "__main__":
    initialize_db()

