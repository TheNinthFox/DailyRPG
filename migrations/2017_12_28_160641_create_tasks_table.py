from orator.migrations import Migration


class CreateTasksTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('tasks') as table:
            table.increments('id')
            table.string('name')
            table.text('description')
            table.big_integer('project_id')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('tasks')
