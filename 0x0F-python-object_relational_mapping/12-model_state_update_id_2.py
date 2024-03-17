#!/usr/bin/python3
"""Sscript that changes the name of a State object
   from the database hbtn_0e_6_usa
"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = sessionmaker()(bind=engine)
    update = session.query(State).where(State.id == 2).first()
    update.name = 'New Mexico'

    session.commit()
