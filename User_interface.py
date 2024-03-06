import tkinter as tk
import Warehouse_Grid as WG
import Inbound_operations_window as inbound
import Outbound_operations_window as outbound
import main as BOSS
#-------------Global Variables--------------
#-------------Main Window----------------

def SaveToFile():
    BOSS.save_to_file()

def OpenFile():
    BOSS.Open_file()
def Inbound():
    inbound.main()

def Outbound():
    outbound.main()



# ------------Creates the WELCOME window
Grid = WG.main()
Main_Menu = tk.Tk()
Main_Menu.title("WAREHOUSE APP 1.0")


name_label = tk.Label(Main_Menu, text=f"You are working in warehouse: {WG.Warehouse[0].name}",font=("Arial 15 bold"))
name_label.pack()
in_button = tk.Button(Main_Menu , text=f"IN Operations",font=("Arial 10 bold"),width=15,anchor="c", bg="gray", padx=10, pady=5,
                                     relief=tk.RAISED,command =Inbound)
out_button = tk.Button(Main_Menu , text=f"OUT Operations",font=("Arial 10 bold"),width=15,anchor="c", bg="gray", padx=10, pady=5,
                                     relief=tk.RAISED, command =Outbound)
Open_file_button = tk.Button(Main_Menu , text=f"Open file",font=("Arial 10 bold"),width=15,anchor="c", bg="gray", padx=10, pady=5,
                                     relief=tk.RAISED,command =OpenFile)
SaveTo_file_button = tk.Button(Main_Menu , text=f"Save to file",font=("Arial 10 bold"),width=15,anchor="c", bg="gray", padx=10, pady=5,
                                     relief=tk.RAISED, command =SaveToFile)

in_button.pack()
out_button.pack()
Open_file_button.pack()
SaveTo_file_button.pack()


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


