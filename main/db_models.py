# coding: utf-8
from sqlalchemy import BigInteger, Float, ForeignKey, Table, Text, Integer, Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.inspection import inspect



Base = declarative_base()
metadata = Base.metadata


t_bank_branches = Table(
    'bank_branches', metadata,
    Column('ifsc', String(11)),
    Column('bank_id', BigInteger),
    Column('branch', String(74)),
    Column('address', String(195)),
    Column('city', String(50)),
    Column('district', String(50)),
    Column('state', String(26)),
    Column('bank_name', String(49))
)

# @dataclass
class Bank(Base):
    __tablename__ = 'banks'

    name = Column(String(49))
    id = Column(Integer, primary_key=True)





class Branch(Base):
    __tablename__ = 'branches'

    ifsc = Column(String(11), primary_key=True)
    bank_id = Column(ForeignKey('banks.id'))
    branch = Column(String(74))
    address = Column(String(195))
    city = Column(String(50))
    district = Column(String(50))
    state = Column(String(26))

    bank = relationship('Bank')

    def serialize(self, ignore=[]):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys() if c not in ignore}
