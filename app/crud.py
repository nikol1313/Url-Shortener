from sqlalchemy.orm import Session
from app.models import URL
from app.schemas import URLCreate
import secrets

def create_url(db: Session, url_data: URLCreate):
    short_code = secrets.token_urlsafe(6)
    db_url = URL(original_url=str(url_data.original_url), short_url=short_code)

    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def get_url(db: Session, short_code: str):
    return db.query(URL).filter(URL.short_url == short_code).first()

