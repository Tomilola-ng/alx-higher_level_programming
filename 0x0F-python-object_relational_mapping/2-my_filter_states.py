#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the
`states` table of the database `hbtn_0e_0_usa` where the `name`
matches the argument (case-sensitive).
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Establish a connection to the database
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    cur.execute(query, (argv[4],))

    # Fetch and print each result
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.close()
