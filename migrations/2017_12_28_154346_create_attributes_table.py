from orator.migrations import Migration


class CreateAttributesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('attributes') as table:
            table.increments('id')
            table.string('name')
            table.text('description')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('attributes')
