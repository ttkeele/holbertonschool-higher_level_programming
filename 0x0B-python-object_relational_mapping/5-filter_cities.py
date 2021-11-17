#!/usr/bin/python3
"""
python script that lists all cities from the database hbtn_0e_4_usa
with specified state name
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv


    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()

    state_lookup = str(argv[4])
    SQL_query = """SELECT cities.name
                   FROM cities
                   LEFT JOIN states
                   ON cities.state_id = states.id
                   WHERE states.name=%s
                   ORDER BY cities.id ASC"""
    cur.execute(SQL_query, (state_lookup,))

    flag = 0
    for row in cur.fetchall():
        if flag == 0:
            flag = 1
        else:
            print(", ", end="")
        print(row[0], end="")
    print()
    db.close()
