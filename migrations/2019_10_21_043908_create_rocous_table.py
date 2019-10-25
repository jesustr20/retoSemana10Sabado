from orator.migrations import Migration


class CreateRocousTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('rocous') as table:
            table.increments('ro_co_us_id')
            table.integer('company_id')
            table.integer('users_id')
            table.integer('role_id')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('rocous')
