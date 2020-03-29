#!/usr/bin/python3
""" List all state objects using sqlalchemy """

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm.session import sessionmaker, Session
from sqlalchemy import create_engine
from sys import argv


if __name__ == '__main__':

    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).\
            order_by(State.id):
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print('\t{}: {}'.format(city.id, city.name))
