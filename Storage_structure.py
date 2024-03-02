





#--------------------------CLASSES-----------------------------------

class W_Shelf():
    def __init__(self,row):
        self.parent = row
        self.shelf_cells =[]
        self.shelf_left = None
        self.shelf_right = None

class W_Cell():
    def __init__(self, shelf):
        assert isinstance(shelf,W_Shelf)
        self.parent = shelf
        self.cell_container =None
        self.cell_above = None
        self.cell_below = None
        self.cell_left = None
        self.cell_right = None
class Warehouse_row():
    def __init__(self, name):
        self.name = name
        self.shelves_in_row = []
        self.cell_above = None
        