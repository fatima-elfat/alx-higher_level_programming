#!/usr/bin/python3
"""
the module of task 13.
"""

from sys import argv
from model_state import Base, State
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
    r = session.query(State).session.query(State).filter(State.name.like('%a%'))
    for row in r:
        session.delete(row)
    session.commit()
    session.close()
