from sqlalchemy import Column, Integer, String
from base import Base

class User(Base):
    """ User info """

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)


    def __init__(self, username, password):
        """ Initializes a user reading """
        self.username = username
        self.password = password
        

    def to_dict(self):
        """ Dictionary Representation of a user reading """
        dict = {}
        dict['username'] = self.username
        dict['password'] = self.password

        return dict