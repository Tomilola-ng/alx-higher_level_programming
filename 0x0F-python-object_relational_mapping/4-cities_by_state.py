#!/usr/bin/python3
"""
This script lists all cities from the database `hbtn_0e_4_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        port=3306,
        passwd=argv[2],
        db=argv[3]
    )

    # Use context manager to handle cursor
    with db.cursor() as cur:
        cur.execute("""
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
        """)

        rows = cur.fetchall()

    # Print each row if available
    if rows:
        for row in rows:
            print(row)
