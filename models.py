from sqlalchemy import create_engine, Column, Integer, String, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

# Определяем таблицу User
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(Enum('alive', 'dead', 'finished', name='status_enum'), default='alive')
    status_updated_at = Column(DateTime, default=datetime.datetime.utcnow)

# Определяем таблицу MessageLog
class MessageLog(Base):
    __tablename__ = 'message_logs'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    message_text = Column(String)
    sent_at = Column(DateTime, default=datetime.datetime.utcnow)