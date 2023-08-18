#!/usr/bin/python3
""" This is a script that uses MySQLdb to lists all states from
the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb


if __name__ == "__main__":
    if len(sys.argv) != 4:
        exit()
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
