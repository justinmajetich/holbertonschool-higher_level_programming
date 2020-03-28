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

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    id_list = []
    for row in session.query(State):
        if 'a' in row.name:
            id_list.append(row.id)

    for id in id_list:
        session.query(State).filter(State.id == id).delete()

    session.commit()
