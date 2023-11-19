#!/usr/bin/python3
"""
the module of task 1.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        db=argv[3],
        user=argv[1],
        passwd=argv[2])
    cr = db.cursor()
    q = """SELECT cities.id, cities.name, states.name
     FROM states
     INNER JOIN cities ON states.id = cities.state_id
     ORDER BY cities.id
    """
    cr.execute(q)
    for row in cr.fetchall():
        print(row)
    cr.close()
    db.close()
