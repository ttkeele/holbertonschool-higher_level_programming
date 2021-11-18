#!/usr/bin/python3
"""
python script that lists all cities from the database hbtn_0e_4_usa
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
    SQL_query = """SELECT cities.id, cities.name, states.name
                   FROM cities
                   LEFT JOIN states
                   ON cities.state_id = states.id
                   ORDER BY cities.id ASC"""
    cur.execute(SQL_query)

    for row in cur.fetchall():
        print(row)
    db.close()
