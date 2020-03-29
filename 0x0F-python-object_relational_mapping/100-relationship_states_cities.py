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

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)

    session.add(new_state)

#   for row in session.query(State, City).all():
#       print(row)
    session.commit()