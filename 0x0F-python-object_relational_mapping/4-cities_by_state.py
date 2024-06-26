#!/usr/bin/python3script 
"""
The scripts that lists all cities from
the database `hbtn_0e_`.
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    """
    Accessing the database and get the cities
    from the database.
    """

    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])

    with db_connect.cursor() as db_cursor:
        db_cursor.execute("SELECT cities.id, cities.name, states.name \
                                FROM cities JOIN states ON cities.state_id \
                                = states.id ORDER BY cities.id ASC")
        rows_selected = db_cursor.fetchall()

    if rows_selected is not None:
        for row in rows_selected:
            print(row)
