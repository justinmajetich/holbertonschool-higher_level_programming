#!/usr/bin/python3
""" Select states starting with N from database """


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

    cursor.execute('SELECT id, name FROM states\
                   WHERE SUBSTRING(name, 1, 1) = \'N\'\
                   ORDER BY states.id ASC')

    for row in cursor.fetchall():
        print(row)
