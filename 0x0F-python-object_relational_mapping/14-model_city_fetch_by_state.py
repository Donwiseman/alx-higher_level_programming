#!/usr/bin/python3
""" A script that uses sqlalchemy to connect to a provided database and
that prints all City objects from the database.
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State.name, City.id, City.name).join(
            City, State.id == City.state_id).all()
    for line in results:
        print(f"{line[0]}: ({line[1]}) {line[2]}")
    session.commit()
    session.close()
