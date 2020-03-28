#!/usr/bin/python3
""" Select states with names matching arguments """


if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db_user = argv[1]
    db_passwd = argv[2]
    db_name = argv[3]

    database = MySQLdb.connect(host='localhost',
                               port=3306,
                               user=db_user,
                               passwd=db_passwd,
                               db=db_name)

    cursor = database.cursor()

    cursor.execute('SELECT cities.id, cities.name, states.name FROM cities\
                   JOIN states\
                   ON cities.state_id = states.id\
                   ORDER BY cities.id ASC')

    for row in cursor.fetchall():
        print(row)
