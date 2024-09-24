#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states table
where `name` matches the argument
from the database `hbtn_0e_0_usa`.

The script is safe from SQL injections.
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
            SELECT *
            FROM states
            WHERE name LIKE BINARY %(name)s
            ORDER BY id ASC
        """, {'name': argv[4]})

        rows = cur.fetchall()

    # Print each row if available
    if rows:
        for row in rows:
            print(row)
