from orator.migrations import Migration


class CreateProductBillTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('product_bill') as table:
            table.increments('Product_bill_id')
            table.integer('product_id')
            table.integer('bill_id')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('product_bill')
