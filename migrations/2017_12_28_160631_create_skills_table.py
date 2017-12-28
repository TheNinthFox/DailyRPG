from orator.migrations import Migration


class CreateSkillsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('skills') as table:
            table.increments('id')
            table.string('name')
            table.text('description')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('skills')
