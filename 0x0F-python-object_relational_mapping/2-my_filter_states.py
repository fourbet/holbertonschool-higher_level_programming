#!/usr/bin/python3
""" Python - Object-relational mapping """
import sys
import MySQLdb

if __name__ == "__main__":
    user_name = sys.argv[1]
    psw = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    conn = MySQLdb.connect(host="localhost", port=3306, user=user_name,
                           passwd=psw, db=db_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(state_name))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
