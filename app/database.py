from pydantic import ConfigDict
from pydantic_settings import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


class Settings(BaseSettings):
    PROJECT_NAME: str = "URL Shortener"
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/dbname"
    model_config = ConfigDict(env_file=".env", extra='ignore')

settings = Settings()

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
