import User_interface as UIS
import Warehouse_Grid as WG
import pandas as pd

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


