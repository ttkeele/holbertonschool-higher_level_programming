#!/usr/bin/python3
"""module updates name of state in database using SQLAlchemy
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import update

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

    list = session.query(State).order_by(State.id).all()
    for obj in list:
        if obj.id == 2:
            obj.name = "New Mexico"
            session.commit()
