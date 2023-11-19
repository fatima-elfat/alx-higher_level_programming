#!/usr/bin/python3
"""
the module of task 15.
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
    Session = sessionmaker(bind=engine)
    session = Session()
    s = State(name="California")
    c = City(name="San Francisco")
    s.cities.append(c)
    session.add(s)
    session.add(c)
    session.commit()
    session.close()
