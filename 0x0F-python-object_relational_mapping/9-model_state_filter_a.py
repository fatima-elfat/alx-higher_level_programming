#!/usr/bin/python3
"""
the module of task 9.
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
    for r in session.query(State).filter(
        State.name.like('%a%')
        ):
        print(r.id, r.name, sep=": ")
