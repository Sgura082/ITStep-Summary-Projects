import tkinter as tk
import Warehouse_Grid as WG
import Storage_structure as Storage
# def submit():
#     name = name_entry.get()
#     age = age_entry.get()
#     print("Name:", name)
#     print("Age:", age)


#-------------Global Variables--------------
global Warehousename
Warehousename = ""
#-------------Main Window----------------
class MAINAPP():
    def __init__(self, master):
        self.master = master
        # Create a frame for the Warehouse
        self.Mainframe = tk.Frame(self.master, bg="black", bd=2, relief=tk.RAISED)
        self.Mainframe.pack(padx=50, pady=20)

def open_warehouse_grid():
    WG.main()
def open_input_window():
    Main_Menu.destroy()
    WG.main()

def open_output_window():
    Main_Menu.destroy()
    WG.main()
def Inbound():
    pass
def Outbound():
    pass


# ------------Creates the WELCOME window
main = WG.main()
Main_Menu = tk.Tk()
Main_Menu.title("WAREHOUSE APP 1.0")


name_label = tk.Label(Main_Menu, text=f"You are working in warehouse: {WG.Warehouse[0].name}",font=("Arial 15 bold"))
name_label.pack()
in_button = tk.Button(Main_Menu , text=f"IN Operations",font=("Arial 10 bold"),width=15,anchor="c", bg="gray", padx=10, pady=5,
                                     relief=tk.RAISED,command =Inbound)
out_button = tk.Button(Main_Menu , text=f"OUT Operations",font=("Arial 10 bold"),width=15,anchor="c", bg="gray", padx=10, pady=5,
                                     relief=tk.RAISED, command =Outbound)
in_button.pack()
out_button.pack()


width = 500
height = 400
ws = Main_Menu.winfo_screenwidth()
hs = Main_Menu.winfo_screenheight()
x = ws/2 -width
y = hs/2 -height-20
Main_Menu.geometry('%dx%d+%d+%d' % (width, height, x, y))

Main_Menu.mainloop()

#-------------Input operation window (putting box into warehouse)

#-------------Output operation window (taking out box out of the warehouse)


