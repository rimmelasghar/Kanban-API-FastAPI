from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from .config import DATABASE_URL

Base = declarative_base()

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
