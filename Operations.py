import Warehouse_Grid as WG
import pandas as pd
import re

global message_to_be_displayed
message_to_be_displayed = None
def store_box_in_warehouse(box,content):
    """
    Searches for a free cell inside the warehouse among its shelves. when such is found cell class method
    put_box_in_cell is called to store the box and its contents within the cell.
    :param box: Number of the stored box can be either string or Box class object.
    :param content: Description of the content of box. String type.
    :return:
    """
    warehouse = WG.Warehouse[0] # gets the main class object (Warehouse, which stores all data about shelves, cells and
                                # their contents
    index = 0
    global message_to_be_displayed
    if len(box) > 6:
        message_to_be_displayed = "Box number cannot have more than 6 digits!!!!\nPlease enter proper Number"
        return
    if re.fullmatch(r"\d+",box)== None:
        message_to_be_displayed = "Box number must contain ONLY digits!!!!\nPlease enter proper Number"
        return
    if len(box) < 6:
        box = "B"+"0"*(6-len(box))+box
    for shelf in warehouse.Shelfs_in_warehouse: #search for free cell in warehouse
        for cell in shelf.shelf_cells:
            if cell.cell_box == None:
                txt = cell.label.cget("text")
                cell.label.configure(text=f"{txt[:5]}: {box}", bg="red")
                cell.put_box_in_cell(box,content)
                message_to_be_displayed = f"Your box N: {box} was stored in cell N: {txt[:5]}"
                return
            index += 1
    message_to_be_displayed = "No free cells were found!!!"
def take_box_frome_warehouse(box):
    warehouse = WG.Warehouse[0]
    global message_to_be_displayed
    if len(box) > 6:
        message_to_be_displayed = "Box number cannot have more than 6 digits!!!!\nPlease enter proper Number"
        return
    if re.fullmatch(r"\d+",box)== None:
        message_to_be_displayed = "Box number must contain ONLY digits!!!!\nPlease enter proper Number"
        return
    if len(box) < 6:
        box = "B"+"0"*(6-len(box))+box
    #search for cell with the box in warehouse
    index = 0
    for shelf in warehouse.Shelfs_in_warehouse:
        for cell in shelf.shelf_cells:
            if cell.cell_box:
                if cell.cell_box.name == box:
                    txt = cell.label.cget("text")
                    cell.label.configure(text=f"{txt[:5]}: FREE", bg="lightgreen")
                    cell.clear_contents()
                    message_to_be_displayed = f"Your box N: {box} was removed from cell N: {txt[:5]}"
                    return
                index += 1
    message_to_be_displayed = "No such BOX was found!!!"

def encoder(warehouse):

    shelf_dict_lst =[]
    for shelf in warehouse.Shelfs_in_warehouse:
        Cells_dict_lst = []
        for cell in shelf.shelf_cells:
            Cells_dict ={"Cell_name": cell.name,
                         "Cell_parent": cell.parent,
                         "Cell_Box": cell.cell_box,
                         "Cell_Status": cell.status,
                         "Cell_Label": cell.label}
            Cells_dict_lst.append(Cells_dict)

        shelf_dict = {"Shelf_Name": shelf.name,
                      "Cells_in_shelf": Cells_dict_lst}
        shelf_dict_lst.append(shelf_dict)
    data = {"Warehouse_name": warehouse.name, "Shelves_in_warehouse": shelf_dict_lst}
    return data
def save_to_file():
    df = pd.DataFrame(encoder(WG.Warehouse[0]))
    df.to_csv('data.csv', index=False)
def Open_file():
    df = pd.read_csv('data.csv', index_col=1)
    a = df.to_dict()
    print(df)
    # for shelf in WG.Warehouse[0].Shelfs_in_warehouse:
    #     for cell in shelf.shelf_cells:

