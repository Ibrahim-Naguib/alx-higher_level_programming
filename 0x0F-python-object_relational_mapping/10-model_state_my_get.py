#!/usr/bin/python3
"""Sscript that prints the State object with the name passed
   as argument from the database hbtn_0e_6_usa
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
    state = session.query(State).filter(State.name == sys.argv[4]).one()

    if not state:
        print("Not found")
    else:
        print("{}".format(state.id))
