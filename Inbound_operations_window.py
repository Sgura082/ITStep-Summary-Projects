import tkinter as tk
import Operations as oper


#---------------------Variables-------------------

#---------------------Classes---------------------
class INwindow():
    def __init__(self,master):
        self.master = master
        #-/--Adds label and entry field for Box number entry-----------------------------------
        Box_number_label = tk.Label(self.master, text="Box number:")
        Box_number_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W, columnspan =2)
        Box_number_entry = tk.Entry(self.master)
        Box_number_entry.grid(row=0, column=3, padx=5, pady=5, columnspan =2) #----/
        #-/--Adds label and entry field for Box number entry-----------------------------------
        Box_content_label = tk.Label(self.master, text="Box content:")
        Box_content_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W, columnspan =2)
        Box_content_entry = tk.Entry(self.master)
        Box_content_entry.grid(row=1, column=3, padx=5, pady=5, columnspan =2)#----/

        # -/--Adds label for system message which displays errors or successful operation status------------------
        System_message_label = tk.Label(self.master, text=f"-----------------------",anchor="w", justify="left",
                                        font=("Arial 10 bold"))
        System_message_label.grid(row=10, column=0, padx=10, pady=5, sticky=tk.W,columnspan=4)

        #------Function used call a function from Operations module which will search and place-------------------
        #--------the box in warehouse cell
        def add_box():
            oper.store_box_in_warehouse(Box_number_entry.get(),Box_content_entry.get())
            System_message_label.configure(text=f"{oper.message_to_be_displayed}",)

        #-----Adds button wich when clicked will use function above
        in_button = tk.Button(self.master, text=f"Store Box", font=("Arial 10 bold"), width=15, anchor="c", bg="gray", padx=10,
                              pady=5,
                              relief=tk.RAISED, command=add_box)
        in_button.grid(row=4, column=1, padx=10, pady=5)

#---------------------Main Code-------------------
def main():
    global root
    root = tk.Tk()
    root.title("Inbound operations")
    window = INwindow(root)
    width = 400
    height = 200
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = ws/2 -width
    y = hs/2 -20
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.mainloop()
if __name__ == "__main__":
    main()

