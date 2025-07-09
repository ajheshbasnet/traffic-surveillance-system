# -- This means table in the database -- #

from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, text
from sqlalchemy.ext.declarative import declarative_base     # -- create tables for the database --#


Base = declarative_base()  # used in models.py 

class Traffic_Database(Base):
    __tablename__ = "citizen_traffic_history"

    plate_no = Column(String, primary_key=True, nullable=False)
    owner_name = Column(String, nullable=False)
    pending_fines = Column(Integer, nullable=False)
    active_charges = Column(Boolean, server_default='FALSE', nullable=False)
    criminal_history = Column(Boolean, server_default='FALSE', nullable=False)
    time = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    