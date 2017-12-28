from orator.migrations import Migration


class CreateAttributesSkillsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('attributes_skills') as table:
            table.increments('id')
            table.big_integer('attribute_id')
            table.big_integer('skill_id')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('attributes_skills')
