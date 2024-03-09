import tkinter as tk
import Warehouse_Grid as WG
import Inbound_operations_window as inbound
import Outbound_operations_window as outbound
import Operations as oper
#-------------Global Variables--------------
#-------------Main Window----------------

def SaveToFile():
    oper.save_to_file()
    System_message_label.configure(text="Your Session was successfully SAVED to file data.json!!!")
def OpenFile():
    oper.Open_file()
    System_message_label.configure(text="Your Session was successfully RETRIEVED from file data.json!!!")
def Inbound(): #Summons window from Inbound_operations_window
    inbound.main()

def Outbound(): #Summons window from Outbound_operations_window
    outbound.main()

# ------------Creates the Main Menu window------------------------------
Grid = WG.main()
Main_Menu = tk.Tk()
Main_Menu.title("WAREHOUSE APP 1.0")


name_label = tk.Label(Main_Menu, text=f"You are working in warehouse: {WG.Warehouse[0].name}",font=("Arial 15 bold"))
name_label.pack()

# ------------Opens Inbound operations window where user can store boxes in warehouse----------------------
in_button = tk.Button(Main_Menu , text=f"IN Operations",font=("Arial 10 bold"),width=15,anchor="c", bg="Green", padx=10, pady=5,
                                     relief=tk.RAISED,command =Inbound)
in_button.pack()

# ------------Opens Outbound operations window where user can take out boxes from warehouse----------------
out_button = tk.Button(Main_Menu , text=f"OUT Operations",font=("Arial 10 bold"),width=15,anchor="c", bg="tomato", padx=10, pady=5,
                                     relief=tk.RAISED, command =Outbound)
out_button.pack()

# ------------Open Json file to retrieve warehouse data from previous session------------------------------
Open_file_button = tk.Button(Main_Menu , text=f"Open file",font=("Arial 10 bold"),width=15,anchor="c", bg="gray",
                             padx=10, pady=5,relief=tk.RAISED,command =OpenFile)
Open_file_button.pack()

# ------------Save current session data to Json file ------------------------------------------------------
SaveTo_file_button = tk.Button(Main_Menu , text=f"Save to file",font=("Arial 10 bold"),width=15,anchor="c", bg="gray",
                               padx=10, pady=5,relief=tk.RAISED, command =SaveToFile)
SaveTo_file_button.pack()

#-------------System message label-------------------------------------------------------------------------
System_message_label = tk.Label(Main_Menu, text=f"---------------------------------------",font=("Arial 10 bold"))
System_message_label.pack()



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


