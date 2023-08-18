#!/usr/bin/python3
""" This is a script that uses MySQLdb to lists all cities available for a
given state which is passed as an argument, using the database hbtn_0e_4_usa
and provides protection against SQL injection attacks.
"""

import sys
import MySQLdb


if __name__ == "__main__":
    if len(sys.argv) != 5:
        exit()
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = """SELECT name FROM cities
                WHERE state_id = (SELECT id FROM states WHERE name = %s)
                ORDER BY id ASC"""
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()
    for num, name in enumerate(rows):
        value = name[0]
        if num == (len(rows) - 1):
            print(value, end='')
        else:
            print(value, end=", ")
    print()
    cur.close()
    db.close()
