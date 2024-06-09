from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Инициализация базы данных
engine = create_engine('sqlite:///funnel.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()