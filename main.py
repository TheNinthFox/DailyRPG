#!/usr/bin/python3

from src.dependency import setup
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    setup()

    from src.dependency import Base, engine
    Base.metadata.create_all(engine)

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    from src.database.models import Skill
    skill_guitar = Skill(name="Guitar", description="The proficiency of your guitar playing.")
    session.add(skill_guitar)
    session.commit()

    skill_guitar_shred = Skill(name="Shredding", description="Your ability to shred", parent=skill_guitar)
    session.add(skill_guitar_shred)
    session.commit()

