from orator.migrations import Migration


class CreateSkillsTasksTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('skills_tasks') as table:
            table.increments('id')
            table.big_integer('skill_id')
            table.big_integer('task_id')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('skills_tasks')
