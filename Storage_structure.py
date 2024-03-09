
import Cell_details_window as CDW
#--------------------------CLASSES-----------------------------------
class Box():
    def __init__(self,name):
        self.name = name
        self.contents = None

    def __str__(self):
        return self.name
class W_Cell():
    def __init__(self, name, label):
        self.name = name
        self.parent = None
        self.cell_box =None
        self.status = "FREE"
        self.cell_above = None
        self.cell_below = None
        self.label = label
        self.label.configure(command=self.show_detail)
    def __str__(self):
        return (f"-------------------\n"
            f"Name: {self.name}, Parent: {self.parent}, Status: {self.status}, Box: {self.cell_box}")
    def show_detail(self):
        CDW.main(self)
    def put_box_in_cell(self,box,box_contents):
        if box == None:
            return
        if isinstance(box,Box):
            self.cell_box = box
        else:
            a = Box(str(box))
            self.cell_box = a
        txt = self.label.cget("text")
        self.label.configure(text=f"{txt[:5]}: {box}", bg="red")
        self.cell_box.contents = box_contents
        self.status = "OCCUPIED"
    def clear_contents(self):
        self.cell_box = None
        txt = self.label.cget("text")
        self.label.configure(text=f"{txt[:5]}: FREE", bg="lightgreen")
        self.status = "FREE"
class W_Shelf():
    def __init__(self,warehouse,name):
        warehouse.Shelfs_in_warehouse.append(self)
        self.name =name
        self.parent = warehouse
        self.first_cell =None
        self.shelf_cells =[]
        # self.shelf_above = None
        # self.shelf_below = None
    def __str__(self):
        return f"{self.name}"
    def add_cell(self,cell):
        cell.parent = self
        if self.first_cell == None:
            self.first_cell = cell
        if self.first_cell == cell:
            self.shelf_cells.append(cell)
            return
        current_cell = self.first_cell
        while current_cell.cell_above:
            current_cell = current_cell.cell_above
        current_cell.cell_above = cell
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