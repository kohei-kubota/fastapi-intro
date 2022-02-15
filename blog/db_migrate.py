from sqlalchemy import create_engine

from .database import Base

DATABASE_URL = 'sqlite:///./blog.db'
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()