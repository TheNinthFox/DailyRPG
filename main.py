#!/usr/bin/python3

from config.db import databases
from src.globals.database import Database

from src.models import *


def create_mock_data():
    draw_everyday = Project()
    draw_everyday.name = 'Draw everyday'
    draw_everyday.description = ''
    draw_everyday.save()

    strength = Attribute()
    strength.name = 'Strength'
    strength.description = ''
    strength.save()

    dexterity = Attribute()
    dexterity.name = 'Dexterity'
    dexterity.description = ''
    dexterity.save()

    drawing = Skill()
    drawing.name = 'Drawing'
    drawing.description = ''
    drawing.save()

    draw_now = Task()
    draw_now.name = 'Draw Now'
    draw_now.description = ''
    draw_everyday.tasks().save(draw_now)

    drawing.attributes().attach(strength)
    drawing.attributes().attach(dexterity)
    drawing.save()

    draw_now.skills().attach(drawing)
    draw_now.save()


if __name__ == '__main__':
    Database.connect(databases)
    # create_mock_data()

    project = Project.find(2)
    print("Project: {}".format(project.name))
    print("Tasks:")
    for task in project.tasks:
        print("  - {}".format(task.name))

        print("  Skills:")
        for skill in task.skills:
            print("    - {}".format(skill.name))

            print("    Attributes:")
            for attribute in skill.attributes:
                print("      - {}".format(attribute.name))

