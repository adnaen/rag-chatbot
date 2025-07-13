from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src.core.settings import settings

engine = create_engine(url=settings.SQLITE_URI)
Session = sessionmaker(bind=engine)
Base = declarative_base()


def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
