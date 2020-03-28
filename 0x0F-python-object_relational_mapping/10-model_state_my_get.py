#!/usr/bin/python3
""" List all state objects using sqlalchemy """

if __name__ == '__main__':

    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm.session import sessionmaker, Session
    from model_state import Base, State

    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    search = argv[4]
    found = 0

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).\
            filter(State.name == search).order_by(State.id):
        if state:
            print('{}'.format(state.id))
            found = 1
    if not found:
        print('Not found')
