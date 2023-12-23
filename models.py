from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy_utils import database_exists, create_database

Base = declarative_base()

class Band(Base):
    __tablename__ = 'Band'

    band_id = Column(Integer, primary_key=True, index=True)
    specialization = Column(String)
    level = Column(Integer)
    status = Column(String)
    nickname = Column(String)
    contact = Column(String)

    robbery = relationship('Robbery', back_populates='band', cascade="all, delete-orphan")

class Robbery(Base):
    __tablename__ = "Robbery"

    robbery_id = Column("robbery_id", Integer, primary_key=True)
    total_sum_for_each = Column("sum", Integer)
    part = Column("part", Integer)
    mark = Column("mark", Integer)

    band_id = Column(Integer, ForeignKey('Band.band_id'), nullable=False)
    bank_id = Column(Integer, ForeignKey('Bank.bank_id'), nullable=False)

    band = relationship('Band', back_populates='robbery')
    bank = relationship('Bank', back_populates='robbery')

class Bank(Base):
    __tablename__ = "Bank"

    bank_id = Column("bank_id", Integer, primary_key=True)
    rate = Column("rate", Integer)
    total_sum = Column("total_sum", Integer)
    address = Column("addres", String)
    security_rate = Column("security_rate", Integer)
    name = Column("name", String)

    robbery = relationship('Robbery', back_populates='bank', cascade="all, delete-orphan")


DATABASE_URL = f'postgresql://arusyak:pass123@localhost:5432/my_project'
engine = create_engine(DATABASE_URL, echo=True)

Base.metadata.create_all(engine)

