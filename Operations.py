
import copy

import pandas as pd

import Warehouse_Grid as WG
import json
import re

global message_to_be_displayed
message_to_be_displayed = None


# --------------------------------------------------------------------------------------------------
def store_box_in_warehouse(box, content):
    """
    Searches for a free cell inside the warehouse among its shelves. when such is found cell class method
    put_box_in_cell is called to store the box and its contents within the cell.
    :param box: Number of the box which is to be stored (string).
    :param content: Description of the content of box. String type.
    :return:
    """
    warehouse = WG.Warehouse[0]  # gets the main class object (Warehouse, which stores all data about shelves, cells and
    # their contents
    index = 0
    global message_to_be_displayed
    if len(box) > 6:
        message_to_be_displayed = "Box number cannot have more than 6 digits!!!!\nPlease enter proper Number"
        return
    if re.fullmatch(r"\d+", box) == None:
        message_to_be_displayed = "Box number must contain ONLY digits!!!!\nPlease enter proper Number"
        return
    if len(box) < 6:
        box = "0" * (6 - len(box)) + box
    box = "B" + box
    for shelf in warehouse.Shelfs_in_warehouse:  # search for free cell in warehouse
        #1-----------------------Checking if box with such number already is stored-----------------
        current_cell = shelf.first_cell
        while True:
            if current_cell.cell_box != None:
                if current_cell.cell_box.name == box:
                    message_to_be_displayed = (f"Box with number {box} is already in warehouse"
                                               f"\nStored in cell {current_cell.name}")
                    return
            if current_cell.cell_above == None:
                break
            current_cell = current_cell.cell_above
        #2------------------------Checking for empty cell--------------------------------------------
        current_cell = shelf.first_cell
        while True:
            if current_cell.cell_box == None:
                txt = current_cell.label.cget("text")
                current_cell.put_box_in_cell(box, content)
                message_to_be_displayed = f"Your box N: {box} was stored in cell N: {txt[:5]}"
                return
            if current_cell.cell_above == None:
                break
            current_cell = current_cell.cell_above
    message_to_be_displayed = "No free cells were found!!!"


# --------------------------------------------------------------------------------------------------
def take_box_frome_warehouse(box):
    """
    Searches for a cell containing the Box class object with the same name  Upon finding one clears the cell contents.
    :param box: The number of a box that needs to be taken out from warehouse.
    :return:
    """
    warehouse = WG.Warehouse[0]
    global message_to_be_displayed
    if len(box) > 6:
        message_to_be_displayed = "Box number cannot have more than 6 digits!!!!\nPlease enter proper Number"
        return
    if re.fullmatch(r"\d+", box) == None:
        message_to_be_displayed = "Box number must contain ONLY digits!!!!\nPlease enter proper Number"
        return
    if len(box) < 6:
        box = "0" * (6 - len(box)) + box
    box = "B" + box
    # search for cell with the box in warehouse
    for shelf in warehouse.Shelfs_in_warehouse:
        for cell in shelf.shelf_cells:
            if cell.cell_box:
                if cell.cell_box.name == box:
                    txt = cell.label.cget("text")
                    cell.clear_contents()
                    message_to_be_displayed = f"Your box N: {box} was removed from cell N: {txt[:5]}"
                    return
    message_to_be_displayed = "No such BOX was found!!!"


# --------------------------------------------------------------------------------------------------
def encoder(warehouse):
    """
    Used to encode cell data for saving to a CSV File
    :param warehouse: Warehouse class object containing information about all cells.
    :return:
    """
    data = []

    for shelf in warehouse.Shelfs_in_warehouse:
        for cell in shelf.shelf_cells:
            Box_name = "None"
            Box_contents = "None"
            if cell.cell_box != None:
                Box_name =cell.cell_box.name
                Box_contents = cell.cell_box.contents
            cell_data = {"Cell_name": cell.name,
                         "Cell_Box_Name": Box_name,
                         "Cell_Box_Contents": Box_contents,
                         "Cell_Status": cell.status}
            cell_datac =copy.deepcopy(cell_data)
            data.append(cell_datac)
    return data


def decoder(data):
    """
    Reads data from saved CSV file and changes existing W_Cell class objects data based on values in file.
    :param data: data (dictionary) from CSV file.
    :return:
    """

    warehouse1 = WG.Warehouse[0]
    print(f"1{warehouse1}")
    for shelf in warehouse1.Shelfs_in_warehouse:
        for cell in shelf.shelf_cells:
            for cell_from_file in data:
                if cell_from_file['Cell_name'] == cell.name:
                    cell_box_name_from_file = cell_from_file['Cell_Box_Name']
                    cell_box_content_from_file = cell_from_file['Cell_Box_Contents']
                    if cell_box_name_from_file == "None":
                        continue
                    cell.put_box_in_cell(cell_box_name_from_file,cell_box_content_from_file)



def save_to_file():
    data = encoder(WG.Warehouse[0])
    with open ('data.json', "w") as csv_file:
        json.dump(data, csv_file)



def Open_file():
    with open ('data.json', "r") as csv_file1:
        data = json.load(csv_file1)
        decoder(data)
