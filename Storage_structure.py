

#--------------------------CLASSES-----------------------------------
class Box():
    def __init__(self,name):
        self.name = name
        self.contents = None
class W_Cell():
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.cell_box =None
        self.status = "FREE"
        self.cell_above = None
        self.cell_below = None
    def __str__(self):
        return (f"Name: {self.name}"
                f"Parent: {self.parent}\n"
                f"cell_box: {self.cell_box}\n"
                f"Cell_above: {self.cell_above}\n"
                f"Cell_below: {self.cell_below}"
                )
    def put_box_in_cell(self,box):
        assert isinstance(box,Box)
        self.cell_box = box
        self.status = "OCCUPIED"
class W_Shelf():
    def __init__(self,warehouse,name):
        self.name =name
        self.parent = warehouse
        self.first_cell =None
        self.shelf_cells =[]
        self.shelf_above = None
        self.shelf_below = None
    def __str__(self):
        return f"{self.name}"
    def add_cell(self,cell):
        cell.parent = self
        if self.first_cell == None:
            self.first_cell = cell
        if self.first_cell == cell:
            return
        current_cell = self.first_cell
        while current_cell.cell_above:
            current_cell = current_cell.above
        current_cell.above = cell
        cell.cell_below = current_cell
        self.shelf_cells.append(cell)
class Warehouse():
    def __init__(self, name):
        self.name = name
        self.Shelfs_in_warehouse = []
    def get_status(self):
        count_of_cells = 0
        for shelf in self.Shelfs_in_warehouse:
            count_of_cells += len(shelf.shelf_cells)

        return f"Total number of cells: {count_of_cells}"