from orator.migrations import Migration


class CreateRoleTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('role') as table:
            table.increments('role_id')
            table.string('name')
            table.string('state')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('role')
