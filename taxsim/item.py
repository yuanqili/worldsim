class Item:

    item_name = 'Generic item'

    def __init__(self, cell):
        self.cell = cell

    def tick(self):
        return


class Food(Item):

    item_name = 'Food'

    def __init__(self, cell=None):
        super().__init__(cell)

    def tick(self):
        return
