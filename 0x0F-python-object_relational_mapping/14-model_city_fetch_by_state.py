#!/usr/bin/python3
"""Script that prints all City objects from the database hbtn_0e_14_usa"""
from model_state import Base, State
from model_city import City
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = sessionmaker()(bind=engine)
    states = session.query(State, City).filter(State.id == City.state_id).all()

    for state, city in states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
