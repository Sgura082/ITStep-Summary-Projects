import tkinter as tk
import math

class BookcaseApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Bookcase")
        # Create a frame for the bookcase
        self.Stellage1_frame = tk.Frame(self.master, bg="lightgray", bd=2, relief=tk.RAISED)
        self.Stellage1_frame.pack( padx=200, pady=20)
        # Create shelves
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
                CN = columnN
            else:
                RN = rowN -4
                CN = 4
            for j in range(3):

                Stellage_title = tk.Label(self.Stellage1_frame, text=f"A0{stellN+1}", bg="white", padx=10, pady=5,
                                          font=("Arial 14 bold"),width=35, height=1)
                Stellage_title.grid(row=RN, column=CN, padx=5, pady=5, columnspan =4)
                Level_title = tk.Label(self.Stellage1_frame, text=f"Level {abs(j-3)} | N: {Stellage_title.cget("text")}.{abs(j-3)}", bg="lightblue", padx=10, pady=5)
                Level_title.grid(row=RN+j+1, column=CN, padx=5, pady=5)

                for i in range(3):
                    shelf1 = tk.Button(self.Stellage1_frame, text=f"{Stellage_title.cget("text")}.{abs(j-3)}.{abs(i+1)}:    FREE", bg="lightgreen", padx=10, pady=5,
                                     relief=tk.RAISED)
                    shelf1.grid(row=RN+j+1, column=CN+i+1, padx=5, pady=5)
                    self.shelves.append(shelf1)
            columnN += 4
            rowN += 4
            stellN += 1



    def add_books(self):
        for i, book in enumerate(self.books):
            shelf_index = i // 2
            book_label = tk.Label(self.shelves[shelf_index], text=book, bg="white", padx=5, pady=2, relief=tk.GROOVE)
            book_label.pack(fill=tk.X)


def main():
    root = tk.Tk()
    root.title("My Database")
    app = BookcaseApp(root)
    root.mainloop()



if __name__ == "__main__":
    main()