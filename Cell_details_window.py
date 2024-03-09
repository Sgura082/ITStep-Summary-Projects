import tkinter as tk
import Operations as oper
import Warehouse_Grid as WG
#---------------------Main Code-------------------


class OUTwindow():
    def __init__(self,master,cell):
        self.master = master
        Cell_name_label = tk.Label(self.master, text=f"CELL N: {cell.name}",font=("Arial 10 bold"),bg="honeydew2")
        Cell_name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        Cell_box_label = tk.Label(self.master, text=f"Stored Box: {cell.cell_box}",font=("Arial 10 bold"))
        Cell_box_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        if cell.cell_box == None:
            contents = "None"
        else:
            contents =cell.cell_box.contents
        Cell_box_Contents_label = tk.Label(self.master, text=f"Box contents: {contents}",font=("Arial 10 bold"))
        Cell_box_Contents_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)


def main(cell):
    root = tk.Tk()
    root.title("Outbound operations")
    window = OUTwindow(root,cell)
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

