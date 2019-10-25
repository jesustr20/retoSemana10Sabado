from orator.migrations import Migration


class CreateBillTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('bill') as table:
            table.increments('bill_id')
            table.integer('invIdenti')
            table.float('unitePrice')
            table.float('igv')
            table.float('totalPrice')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('bill')
