from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:password2025@localhost:3306/products_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base = declarative_base()