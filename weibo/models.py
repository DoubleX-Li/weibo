from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    uid = Column(String(255))
    name = Column(String(20))
    gender = Column(String(10))
    location = Column(String(255))
    intro = Column(String(255))
    signin = Column(String(255))
    school = Column(String(255))
    company = Column(String(255))

    def __init__(self, uid, name, gender, location, intro, signin, school, company):
        self.uid = uid
        self.name = name
        self.gender = gender
        self.location = location
        self.intro = intro
        self.signin = signin
        self.school = school
        self.company = company

    def __repr__(self):
        return 'User: %r' % self.name
