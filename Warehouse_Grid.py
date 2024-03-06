import tkinter as tk
import Storage_structure as Storage

#--------------------------CLASSES-----------------------------------
class WarehouseApp:
    def __init__(self, master):
        self.warehouse_struct = Storage.Warehouse("W01")
        self.master = master
        self.master.title("Bookcase")
        # Create a frame for the Warehouse
        self.Warehouse_frame = tk.Frame(self.master, bg="black", bd=2, relief=tk.RAISED)
        self.Warehouse_frame.pack( padx=50, pady=20)
        # Create a frame for the shelves
        self.shelves = []
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
                CN = 5
            self.Shelf_frame = tk.Frame(self.Warehouse_frame, bg="lightgray", bd=2, relief=tk.SUNKEN)
            self.Shelf_frame.grid(row=RN, column=CN, padx=10, pady=3, columnspan =4)

            Shelf_title = tk.Label(self.Shelf_frame, text=f"A0{stellN + 1}", bg="skyblue", padx=10, pady=5,
                                   font=("Arial 14 bold"), width=20, height=1, relief=tk.RAISED)
            Shelf_title.grid(row=RN, column=CN, padx=5, pady=3, columnspan=4)
            shelf_new = Storage.W_Shelf(self.warehouse_struct,f"A0{stellN + 1}")
            self.warehouse_struct.Shelfs_in_warehouse.append(shelf_new)
            for j in range(3):


                Level_title = tk.Label(self.Shelf_frame , text=f"Level {abs(j-3)}", bg="lightblue", padx=10, pady=5)
                Level_title.grid(row=RN+j+1, column=CN, padx=5, pady=3)



                shelf_cell = tk.Button(self.Shelf_frame , text=f"{Shelf_title.cget("text")}.{abs(j-3)}:    FREE",width=15,anchor="w", bg="lightgreen", padx=10, pady=5,
                                     relief=tk.RAISED)
                shelf_cell.grid(row=RN+j+1, column=CN+1, padx=5, pady=3)
                cell_new = Storage.W_Cell(shelf_cell.cget("text"))
                self.shelves.append(shelf_cell)
                shelf_new.add_cell(cell_new)
            columnN += 4
            rowN += 4
            stellN += 1
        Row_lane = tk.Label(self.Warehouse_frame, bg="gold", padx=3, pady=3,
                                width=1, height=50)
        Row_lane.grid(row=0, column=4, padx=1, pady=1, rowspan=RN*2)

    def search_for_empty(self):
        current_cell = None

    def insert_containers(self):
        shelf_index = 1
        cell_name =self.shelves[shelf_index].cget("text")[:9]
        self.shelves[shelf_index].config(text=f"{cell_name}OCCUPIED",bg="RED",relief=tk.SUNKEN)


#--------------------------Main Code-----------------------------------
def main():
    root = tk.Tk()
    root.title("My Database")
    app = WarehouseApp(root)
    a= app.warehouse_struct.Shelfs_in_warehouse
    for i in a:
        print(i)
    app.insert_containers()
    root.mainloop()
# def load_container(cont):


if __name__ == "__main__":
    main()