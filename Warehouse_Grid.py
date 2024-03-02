import tkinter as tk
import math

#--------------------------CLASSES-----------------------------------
class WarehouseApp:
    def __init__(self, master):
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
            for j in range(3):

                Shelf_title = tk.Label(self.Shelf_frame , text=f"A0{stellN+1}", bg="skyblue", padx=10, pady=5,
                                          font=("Arial 14 bold"),width=38, height=1,relief=tk.RAISED)
                Shelf_title.grid(row=RN, column=CN, padx=5, pady=3, columnspan =4)

                Level_title = tk.Label(self.Shelf_frame , text=f"Level {abs(j-3)} | #{Shelf_title.cget("text")}.{abs(j-3)}", bg="lightblue", padx=10, pady=5)
                Level_title.grid(row=RN+j+1, column=CN, padx=5, pady=3)


                for i in range(3):
                    shelf1 = tk.Button(self.Shelf_frame , text=f"{Shelf_title.cget("text")}.{abs(j-3)}.{abs(i+1)}:    FREE", bg="lightgreen", padx=10, pady=5,
                                     relief=tk.RAISED)
                    shelf1.grid(row=RN+j+1, column=CN+i+1, padx=5, pady=3)
                    self.shelves.append(shelf1)
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

        print(cell_name)
        self.shelves[shelf_index].config(text=f"{cell_name}OCCUPIED",bg="RED",relief=tk.SUNKEN)


#--------------------------Main Code-----------------------------------
def main():
    root = tk.Tk()
    root.title("My Database")
    app = WarehouseApp(root)
    app.insert_containers()
    root.mainloop()
# def load_container(cont):



if __name__ == "__main__":
    main()