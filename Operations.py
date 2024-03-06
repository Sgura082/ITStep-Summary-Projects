import Warehouse_Grid as WG

global message_to_be_displayed
message_to_be_displayed = ""
def store_box_in_warehouse(box,content):
    warehouse = WG.Warehouse[0]
    #search for free cell in warehouse
    index = 0
    for shelf in warehouse.Shelfs_in_warehouse:
        for cell in shelf.shelf_cells:
            if cell.cell_box == None:
                txt = cell.label.cget("text")
                cell.label.configure(text=f"{txt[:5]}: {box}", bg="red")
                cell.put_box_in_cell(box)
                cell.cell_box.contents =content
                global message_to_be_displayed
                message_to_be_displayed = f"Your box N: {box} was stored in cell N: {txt[:5]}"
                return
            index += 1
    message_to_be_displayed = "No free cells were found!!!"
def take_box_frome_warehouse(box):
    warehouse = WG.Warehouse[0]
    #search for cell with the box in warehouse
    index = 0
    for shelf in warehouse.Shelfs_in_warehouse:
        for cell in shelf.shelf_cells:
            if cell.cell_box:
                if cell.cell_box.name == box:
                    txt = cell.label.cget("text")
                    cell.label.configure(text=f"{txt[:5]}: FREE", bg="lightgreen")
                    cell.clear_contents()
                    global message_to_be_displayed
                    message_to_be_displayed = f"Your box N: {box} was removed from cell N: {txt[:5]}"
                    return
                index += 1
    message_to_be_displayed = "No such BOX was found!!!"

