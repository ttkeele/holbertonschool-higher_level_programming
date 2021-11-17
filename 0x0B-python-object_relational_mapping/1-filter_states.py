#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa with a name
starting with N
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
                    WHERE BINARY states.name LIKE 'N%'
                    ORDER BY states.id ASC"""
    cur.execute(SQLcommand)

    for row in cur.fetchall():
        print(row)
    db.close()
