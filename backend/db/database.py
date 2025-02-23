import urllib
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from constants.constants import POSTGRES_HOST, POSTGRES_PORT, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB

class Database:

    def __init__(self) -> None:
        host = urllib.parse.quote(str(POSTGRES_HOST))
        port = urllib.parse.quote(str(POSTGRES_PORT))
        username = urllib.parse.quote(str(POSTGRES_USER))
        password = urllib.parse.quote(str(POSTGRES_PASSWORD))
        db = urllib.parse.quote(str(POSTGRES_DB))
        self.conn_str = f"postgresql://{username}:{password}@{host}:{port}/{db}"
        print(self.conn_str)

    def get_engine(self):
        try:
            engine = create_engine(self.conn_str, echo=True)
            return engine
        except Exception as e:
            print(f"Could not create database engine. Something went wrong: {str(e)}")

    def get_base(self):
        Base = declarative_base()
        return Base
    
    def get_session(self):
        engine = self.get_engine()
        SessionLocal = sessionmaker(bind=engine)
        return SessionLocal
    
# Dependency to get the database session
def get_db():
    db = Database().get_session()
    try:
        yield db()
    finally:
        db().close()