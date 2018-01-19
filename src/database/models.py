from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation

Base = declarative_base()


class Skill(Base):
    __tablename__ = 'skill'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text, nullable=False)
    parent_id = Column(Integer, ForeignKey('skill.id'), nullable=True)

    parent = relation('Skill', remote_side=[id], backref='children')

    def __repr__(self):
        return "<Skill(name='%s', description='%s')>a" % (self.name, self.description)
