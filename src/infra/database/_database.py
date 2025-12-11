from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.settings import Setting


class TouristAIDatabase():
    """
    TouristAI Database
    ------------------
    - Database connection settings
    - Use PostgreSQL in Docker
    """
    def __init__(self):
        settings = Setting()
        host = settings.POSTGRES_HOST.get_secret_value()
        user = settings.POSTGRES_USER.get_secret_value()
        password = settings.POSTGRES_PASSWORD.get_secret_value()
        db = settings.POSTGRES_DB.get_secret_value()
        self.database_url = f"postgresql://{user}:{password}@{host}:5432/{db}"


database = TouristAIDatabase()

# SQLAlchemy engine
engine = create_engine(database.database_url)

# Session factory
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()


def get_db():
    db = Session()
    
    try:
        yield db
    finally:
        db.close()
