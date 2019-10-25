from orator.migrations import Migration


class CreateCompanyTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('company') as table:
            table.increments('company_id')
            table.string('ruc')
            table.string('name')
            table.string('address')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('company')
