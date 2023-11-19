#!/usr/bin/python3
"""
the module of task 16.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    db = argv[3]
    user = argv[1]
    passwd = argv[2]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for r in session.query(State).order_by(State.id).all():
        print(r.id, r.name, sep=": ")
        for c in r.cities:
            print("    ", end="")
            print(c.id, c.name, sep=": ")
    session.close()
