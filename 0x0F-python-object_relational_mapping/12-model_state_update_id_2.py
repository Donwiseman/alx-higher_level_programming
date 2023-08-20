#!/usr/bin/python3
""" A script that uses sqlalchemy to connect to a provided database and
changes the name of a State object at id = 2 from the database hbtn_0e_6_usa
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
    new_st = session.query(State).filter(State.id == 2).first()
    new_st.name = "New Mexico"
    session.commit()
    session.close()
