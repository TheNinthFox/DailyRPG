from orator.migrations import Migration


class UpdateTasksTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('tasks') as table:
            table.string('name').nullable().change()
            pass

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('tasks') as table:
            table.string('name').change()
            pass
