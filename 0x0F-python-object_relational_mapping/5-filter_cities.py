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
    cur.execute("SELECT DISTINCT cities.name FROM cities WHERE cities.state_id\
    = (SELECT states.id FROM states WHERE states.name = %(name)s\
    ORDER BY cities.id)", {'name': state_name})
    query_rows = cur.fetchall()
    count = 0
    for row in query_rows:
        if (count < len(query_rows) - 1):
            print(row[0], end=", ")
        else:
            print(row[0])
        count += 1
    print("")
    cur.close()
    conn.close()
