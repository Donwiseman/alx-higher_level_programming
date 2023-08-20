#!/usr/bin/python3
""" A script that uses sqlalchemy to connect to a provided database and
creates the State “California” with the City “San Francisco” from the database.
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_st = State(name="California")
    new_st.cities = [City(name="San Francisco")]
    session.add(new_st)
    session.commit()
    session.close()
