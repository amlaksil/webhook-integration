#!/usr/bin/python3
"""
Database models and session management for transactions.
"""

from datetime import datetime
from os import getenv
from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP
from sqlalchemy import event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = getenv("DATABASE_URL", "")

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# pylint: disable=too-few-public-methods
class Transaction(Base):
    """
    Model representing a financial transaction
    """
    __tablename__ = 'transactions'
    id = Column(String, primary_key=True)
    amount = Column(Integer)
    currency = Column(String(3))
    created_at_time = Column(TIMESTAMP)
    timestamp = Column(TIMESTAMP)
    cause = Column(String)
    full_name = Column(String)
    account_name = Column(String)
    invoice_url = Column(String)

@event.listens_for(Transaction, "before_insert")
def convert_unix_timestamps(_mapper, _connection, target):
    """
    Convert integer timestamps to datetime before inserting
    """
    if isinstance(target.created_at_time, int):
        target.created_at_time = datetime.fromtimestamp(target.created_at_time)
    if isinstance(target.timestamp, int):
        target.timestamp = datetime.fromtimestamp(target.timestamp)

def get_session():
    """
    Return a new session for database interaction
    """
    return Session()

def init_db():
    """
    Create all tables in the database
    """
    Base.metadata.create_all(engine)
