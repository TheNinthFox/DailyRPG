from orator import Model
from orator.orm import has_many
from orator.orm import belongs_to
from orator.orm import belongs_to_many


class Attribute(Model):

    @belongs_to_many
    def skills(self):
        return Skill


class Skill(Model):

    @belongs_to_many
    def attributes(self):
        return Attribute

    @belongs_to_many
    def tasks(self):
        return Task


class Task(Model):

    @belongs_to_many
    def skills(self):
        return Skill

    @belongs_to
    def project(self):
        return Project


class Project(Model):

    @has_many
    def tasks(self):
        return Task
