#!/usr/bin/python3
"""
prints the State object with the name passed as argument from a database
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":

    username = argv[1]
    passwd = argv[2]
    db = argv[3]
    state_obj = argv[4]

    engine_string = "mysql://{}:{}@localhost:3306/{}".format(username,
                                                             wd, db)
    engine = create_engine(engine_string)
    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    list = session.query(State).order_by(State.id).all()
    found_flag = 0
    for obj in list:
        if obj.name == state_obj:
            print("{}".format(obj.id))
            found_flag = 1
        if found_flag == 0:
            print("Not found")
