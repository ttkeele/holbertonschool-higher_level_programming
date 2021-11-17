#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa with a
given name and is safe from MySQL injections
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

    SQLcommand = """SELECT * FROM states
                    WHERE BINARY states.name LIKE '{}'
                    ORDER BY states.id ASC""".format(argv[4])

    cur.execute(SQLcommand)

    for row in cur.fetchall():
        print(row)
    db.close()
