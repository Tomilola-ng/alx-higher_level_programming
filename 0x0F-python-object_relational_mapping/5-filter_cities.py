#!/usr/bin/python3
"""
This script takes in the name of a state as an argument and lists all cities
of that state, using the database `hbtn_0e_4_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Ensure the correct number of arguments is provided
    if len(argv) != 5:
        print("Usage: ./script.py <mysql username> <mysql password> <database> <state name>")
        exit(1)

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
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name LIKE BINARY %(state_name)s
            ORDER BY cities.id ASC
        """, {'state_name': argv[4]})

        rows = cur.fetchall()

    # Print city names or a message if no cities found
    if rows:
        print(", ".join([row[0] for row in rows]))
    else:
        print("No cities found.")
