#!/usr/bin/python3
"""
adds the State object Louisiana to a database
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    username = argv[1]
    passwd = argv[2]
    db = argv[3]

    engine_string = "mysql://{}:{}@localhost:3306/{}".format(username,
                                                             passwd, db)

    engine = create_engine(engine_string)
    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    list = session.query(State).order_by(State.id).all()
    found_flag = 0
    for obj in list:
        if obj.name == 'Louisiana':
            print("{}".format(obj.id))
            found_flag = 1
        if found_flag == 0:
            print("Not found")
