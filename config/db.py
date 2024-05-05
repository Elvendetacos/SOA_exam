from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

conection = os.getenv('URIDB')
user = os.getenv('USERDB')
password = os.getenv('PSSWDB')

engine = create_engine(f'mysql+pymysql://{user}:{password}@{conection}:3306/school_management')
meta = MetaData()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
conn = engine.connect()
