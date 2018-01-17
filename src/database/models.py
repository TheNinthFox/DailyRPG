from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relation
from ..dependency import Base


class Skill(Base):
    __tablename__ = 'skill'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text, nullable=False)
    parent_id = Column(Integer, ForeignKey('skill.id'), nullable=True)

    parent = relation('Skill', remote_side=[id], backref='children')

    def __repr__(self):
        return "<Skill(name='%s', description='%s')>a" % (self.name, self.description)
