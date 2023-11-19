#!/usr/bin/python3
"""
the module of task 14.
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    db = argv[3]
    user = argv[1]
    passwd = argv[2]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db))
    Session = sessionmaker(bind=engine)
    session = Session()
    r = session.query(State.name, City.id, City.name).filter(
        State.id == City.state_id)
    for row in r:
        print("{:s}: ({:d}) {:s}".format(r[0], r[1], r[2]))
    session.close()
