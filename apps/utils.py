import enum
from apps.database.connection import SessionLocal


class ContentType(enum.Enum):
    serial = 1
    movie = 2


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
