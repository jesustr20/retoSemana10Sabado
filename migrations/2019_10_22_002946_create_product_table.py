from orator.migrations import Migration


class CreateProductTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('product') as table:
            table.increments('product_id')
            table.string('name')
            table.float('price')
            table.integer('quantity')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('product')
