import tkinter as tk
import Operations as oper
#---------------------Main Code-------------------


class INwindow():
    def __init__(self,master):
        self.master = master
        Box_number_label = tk.Label(self.master, text="Box number:")
        Box_number_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        Box_number_entry = tk.Entry(self.master)
        Box_number_entry.grid(row=0, column=1, padx=10, pady=5)

        Box_content_label = tk.Label(self.master, text="Box content:")
        Box_content_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        Box_content_entry = tk.Entry(self.master)
        Box_content_entry.grid(row=1, column=1, padx=10, pady=5)
        def add_box():
            oper.store_box_in_warehouse(Box_number_entry.get())
        in_button = tk.Button(self.master, text=f"Store Box", font=("Arial 10 bold"), width=15, anchor="c", bg="gray", padx=10,
                              pady=5,
                              relief=tk.RAISED, command=add_box)
        in_button.grid(row=4, column=1, padx=10, pady=5)

def main():
    global root
    root = tk.Tk()
    root.title("Inbound operations")
    window = INwindow(root)
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

