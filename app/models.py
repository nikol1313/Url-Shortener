from sqlalchemy.orm import mapped_column, Mapped
from app.database import Base

class URL(Base):
    __tablename__ = "urls"

    id : Mapped[int] = mapped_column(primary_key=True ,index=True)
    original_url: Mapped[str] = mapped_column(nullable=False, index=True)
    short_url: Mapped[str] = mapped_column(nullable=False, index=True, unique=True)

