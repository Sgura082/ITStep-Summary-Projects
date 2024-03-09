import tkinter as tk
import Storage_structure as Storage


#--------------------------VARIABLES---------------------------------
global Warehouse, Wgrid
Warehouse = []
Wgrid = []
#--------------------------Functions---------------------------------

#--------------------------CLASSES-----------------------------------
class WarehouseApp:
    def __init__(self, master):
        self.warehouse_struct = Storage.Warehouse("W01")
        global Warehouse
        Warehouse.append(self.warehouse_struct)
        self.master = master
        # Create a frame for the Warehouse-------------------------------------------------------
        self.Warehouse_frame = tk.Frame(self.master, bg="black", bd=2, relief=tk.RAISED)
        self.Warehouse_frame.pack( padx=50, pady=20)
        self.shelves = [] #Used to store data about created shelf frames below

        #/-------used to decide on which row the shelf will be placed: Odd numbered on left - Even on the right.
        # -------Counts the number of rows and columns  on warehouse frame. On each row only one line of shelf
        # -------frames are placed.
        columnN = 0
        rowN = 0
        stellN = 0
        for num_of_Stell in range(8):
            if stellN % 2 == 0:
                RN = rowN
                CN = 0
            elif stellN <2:
                RN = 0
                CN = 5
            else:
                RN = rowN - 4
                CN = 5 #-------------------/

            # --------Create a sub-frame for the shelves---------------------------------------------
            self.Shelf_frame = tk.Frame(self.Warehouse_frame, bg="lightgray", bd=2, relief=tk.SUNKEN)
            self.Shelf_frame.grid(row=RN, column=CN, padx=10, pady=3, columnspan =4)
            Shelf_title = tk.Label(self.Shelf_frame, text=f"A0{stellN + 1}", bg="skyblue", padx=10, pady=5,
                                   font=("Arial 14 bold"), width=20, height=1, relief=tk.RAISED)
            Shelf_title.grid(row=RN, column=CN, padx=5, pady=3, columnspan=4)

            #/---Creates W_shelf class object to store data about cells and stored boxes by ------------
            # ---grouping them together as shelves------------------------------------------------------
            shelf_new = Storage.W_Shelf(self.warehouse_struct,f"A0{stellN + 1}") #---/


            # Add level titles and Cell buttons to the Shelf Frame--------------------------------------------------
            number_of_level_on_shelf = 3 #only 3 leveled shelfs are formed
            for j in range(number_of_level_on_shelf):
                Level_title = tk.Label(self.Shelf_frame , text=f"Level {abs(j-3)}", bg="lightblue", padx=10, pady=5)
                Level_title.grid(row=RN+j+1, column=CN, padx=5, pady=3)
                shelf_cell = tk.Button(self.Shelf_frame , text=f"{Shelf_title.cget("text")}.{abs(j-3)}: FREE",width=15,anchor="w", bg="lightgreen", padx=10, pady=5,
                                     relief=tk.RAISED)
                shelf_cell.grid(row=RN+j+1, column=CN+1, padx=5, pady=3)


                #Creates W_Cell class object which will store data of stored products and button info.
                # This initialisation of W_Cell also adds function to the button (opening cell details window)
                cell_new = Storage.W_Cell(shelf_cell.cget("text")[:5],shelf_cell)

                #-/--Since shelves are added from the top to bottom the first floor cell is always
                # ---formed last, so this code makes sure last added cell is the first one in the shelf cell list
                self.shelves.insert(0,shelf_cell) #---/

                #-/--Adds W_Cell class object to the W_Shelf class object attribute thus building a linked list.
                shelf_new.add_cell(cell_new) #---/
            #-/--After creating and adding all the titles and cells to shelf frame these variables are
            # ---incremented by their numebrs so that new shelf frame will be placed properly on warehouse frame.
            columnN += 4
            rowN += 4
            stellN += 1 #---/

        #Just for visualisation of walking path for employees
        Row_lane = tk.Label(self.Warehouse_frame, bg="lemonChiffon2", padx=3, pady=3,
                                width=1, height=50)
        Row_lane.grid(row=0, column=4, padx=1, pady=1, rowspan=RN*2)

#--------------------------Main Code-----------------------------------

def main():
    root = tk.Tk()
    app = WarehouseApp(root)
    root.title(f"WAREHOUSE {Warehouse[0].name} STATUS")
    width = 720
    height = 800
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x=ws-width
    y=hs - height-20
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
# def load_container(cont):
if __name__ == "__main__":
    main()


