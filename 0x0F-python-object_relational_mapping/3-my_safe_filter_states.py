#!/usr/bin/python3
"""
The script takiung in an argument and
displaying  values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
This time the script is safe from
MySQL injections!
"""

import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    """
    Accessing the database and getting the states
    from the database as well.
    """
    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()
    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
