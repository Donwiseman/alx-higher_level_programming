#!/usr/bin/python3
""" A script that uses sqlalchemy to connect to a provided database and
printss the State object with the name passed as argument if present.
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    found = False
    for instance in session.query(State.id).filter(State.name == sys.argv[4]):
        print(instance.id)
        found = True
    if (not found):
        print("Not found")
    session.close()
