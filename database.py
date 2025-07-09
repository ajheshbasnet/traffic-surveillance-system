from sqlalchemy import create_engine                        # -- connects app to the database --#
from sqlalchemy.orm import sessionmaker                     # -- helps to establish session to the database -- #


SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:user@localhost/traffic_history' ## SAME AS DOING psycopg2.connect()


engine = create_engine(SQLALCHEMY_DATABASE_URL,
    pool_size=10,       
    max_overflow=20,     
    pool_timeout=30,     
    pool_recycle=1800    
)
SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind = engine) # -- this line tells which database to connect --#

def get_db(): # to establish the session with the database. copy paste from documentation.
    db = SessionLocal()
    return db