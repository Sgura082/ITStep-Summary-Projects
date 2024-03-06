import tkinter as tk
import Operations as oper
import Warehouse_Grid as WG
#---------------------Main Code-------------------


class OUTwindow():
    def __init__(self,master):
        self.master = master
        Box_number_label = tk.Label(self.master, text="Box number:")
        Box_number_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        Box_number_entry = tk.Entry(self.master)
        Box_number_entry.grid(row=0, column=1, padx=10, pady=5)

        def take_box():
            oper.take_box_frome_warehouse(Box_number_entry.get())
        in_button = tk.Button(self.master, text=f"Take out the Box", font=("Arial 10 bold"), width=15, anchor="c", bg="gray", padx=10,
                              pady=5,
                              relief=tk.RAISED, command=take_box)
        in_button.grid(row=4, column=1, padx=10, pady=5)

def main(data):
    root = tk.Tk()
    root.title("Outbound operations")
    window = OUTwindow(root)
    width = 500
    height = 400
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = ws/2 -width
    y = hs/2 -20
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.mainloop()
if __name__ == "__main__":
    main()

