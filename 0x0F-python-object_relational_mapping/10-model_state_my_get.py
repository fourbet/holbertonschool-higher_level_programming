#!/usr/bin/python3
""" Python - Object-relational mapping"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_name = sys.argv[4]
    ok = 0
    for state in session.query(State).order_by(State.id).all():
        if state_name == state.name:
            print(state.id)
            ok = 1
    if ok == 0:
        print("Not found")
    session.close()
