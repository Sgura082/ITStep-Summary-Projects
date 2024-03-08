import re

# --------------------TASK DESCRIPTIONS-------------------------------
# ------Task1: Calculator
# ------Task2: Library management
# ------Task3:
# ------Task4:


# -----------GLOBAL Variables----------------
global Task_list
Task_list = []


# -----------MAIN CLASSES----------------
class Task():
    def __init__(self, name):
        assert isinstance(name, str), "'name' must be a string!!!"
        self.Function = object
        Task_list.append(self)
        self.name = f"Task{Task_list.index(self) + 1}: {name}"

    def __str__(self):
        return self.name

    def write_function(self, object101):
        self.Function = object101

    def __call__(self):
        Looper = "y"
        while Looper == "y":
            self.Function()
            Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
            if Replay == "y":
                continue
            else:
                Looper = Replay


# -----------CUSTOM FUNCTIONS----------------

# -----------TASK OBJECTS----------------
Task01 = Task("Calculator")


def task1_body():
    pass
    # ----------------Task Variables----------------------------------
    Calculator = {'+': {"Name": "   Addition", "Formula": lambda x, y: x + y},
                  '-': {"Name": "   Subtraction", "Formula": lambda x, y: x - y},
                  '/': {"Name": "   Division", "Formula": lambda x, y: x / y},
                  '*': {"Name": "   Multiplication", "Formula": lambda x, y: x * y},
                  '//': {"Name": "  Floor division", "Formula": lambda x, y: x // y},
                  '%': {"Name": "   Modulus", "Formula": lambda x, y: x % y},
                  '**': {"Name": "  Exponentiation", "Formula": lambda x, y: x ** y},
                  'root': {"Name": "Getting root", "Formula": lambda x, y: x ** (1 / y)}}

    # ----------------Task Classes------------------------------------
    # ----------------Task Functions----------------------------------
    def input_loop_with_validation(N, opera=""):
        Control_for_zero_division = ["/", "//", "%"]
        while True:
            userNum = input(f"Enter number {N}: ")
            if (opera in Control_for_zero_division) and float(userNum) == 0:
                print("You can't divide by 0. Enter other number!!!")
                continue
            elif re.match(r'^([\.\d]+)$', userNum):
                break
            else:
                print("ERROR Wrong input. Please enter only INT number.")
        return userNum

    # ----------------Task BODY---------------------------------------
    print("\n-----------------------------------")
    OperationList = list(Calculator.keys())
    prompt = [" " + i + " " + Calculator.get(i).get("Name") for i in OperationList]
    print("\n------PROMPT LIST------", *prompt, sep="\n")
    while True:
        userOper = input("\nEnter an operation you want to conduct (use prompt above): ")
        if userOper in OperationList:
            break
        else:
            print("No such operation found!!! Check prompt list at the start of program!!")
    userNum1 = float(input_loop_with_validation(1))
    userNum2 = float(input_loop_with_validation(2, userOper))
    result = Calculator.get(userOper).get("Formula")(userNum1, userNum2)
    print(f"\nResult of calculation: \n{userNum1} {userOper} {userNum2} = {result}")


Task01.write_function(task1_body)

# -------------------------------------------------------------------------------------------

Task02 = Task("Library management")


def task2_body():
    pass

    # ----------------Task Variables----------------------------------
    # ----------------Task Classes------------------------------------
    class Book():
        def __init__(self, title, author, issue_date, genre, rating):
            self.title = title
            self.author = author
            self.issue_date = issue_date
            self.genre = genre
            self.critics_rating = rating  # Rating of a book from min 1 to max 5
            self.borrower = None  # Name of person who borrowed the book from the library
            self.status = "IN Library"
            self.time_out_of_library = 0.0  # Time the book spent outside library while being borrowed by the reader
        def __str__(self):
            return (f"Title: {self.title}, Author: {self.author}, "
                    f"Issue Date: {self.issue_date}, Genre: {self.genre}, Rating: {self.critics_rating}")

    class Reader():
        def __init__(self, name, id, student_status):
            self.name = name
            self.id = id
            self.student_status = student_status

    class Library():
        def __init__(self, name):
            self.name = name
            self.book_list = []
            self.book_borrowers = {'white_list': [{'Borrower': object,
                                                   'Number of books borrowed': 0,
                                                   'Number of overdue books': 0}],
                                   'blacklist': [{'Borrower': object,
                                                  'Number of books borrowed': 0,
                                                  'Number of overdue books': 0}],
                                   }

        def add_book(self, book):
            assert isinstance(book, Book)
            self.book_list.append(book)

        def search_and_disp_books(self, title="", author="", issue_date="", genre="", rating=""):
            display_list = []
            if title == "":
                title_search = 0
            else:
                title_search = 1
            if author == "":
                author_search = 0
            else:
                author_search = 1
            if issue_date == "":
                issue_date_search = 0
            else:
                issue_date_search = 1
            if genre == "":
                genre_search = 0
            else:
                genre_search = 1
            if rating == "":
                rating_search = 0
            else:
                rating_search = 1
            search_pattern = [title_search, author_search, issue_date_search, genre_search, rating_search]
            for book in self.book_list:
                current_book_patter_validation = []
                if title in book.title or title_search == 0:
                    current_book_patter_validation.append(1)
                else:
                    current_book_patter_validation.append(0)
                if author in book.author or author_search == 0:
                    current_book_patter_validation.append(1)
                else:
                    current_book_patter_validation.append(0)
                if issue_date == book.issue_date or issue_date_search == 0:
                    current_book_patter_validation.append(1)
                else:
                    current_book_patter_validation.append(0)
                if genre == book.genre or genre_search == 0:
                    current_book_patter_validation.append(1)
                else:
                    current_book_patter_validation.append(0)
                if rating < book.rating or rating_search == 0:
                    current_book_patter_validation.append(1)
                else:
                    current_book_patter_validation.append(0)
                #checks if the bookk satisfies the needed search pattern
                if search_pattern == current_book_patter_validation:
                    display_list.append(book)
            return display_list
        def display_all_books(self):
            display_list = []
            for book in self.book_list:
                print(f"{self.book_list.index(book)+1}: {book}")

    # ----------------Task Functions----------------------------------
    # ----------------Task BODY---------------------------------------


Task02.write_function(task2_body)

# -------------------------------------------------------------------------------------------
Task03 = Task("x")


def task3_body():
    pass
    # ----------------Task Variables----------------------------------
    # ----------------Task Classes------------------------------------
    # ----------------Task Functions----------------------------------
    # ----------------Task BODY---------------------------------------


Task03.write_function(task3_body)

# -------------MAIN CODE---------------------------------------------------------------------

for task in Task_list:
    Task_status = input(f"\nDo you want to do - {task}? \n(Enter 'y' for YES or any key for NO) ")
    if Task_status == "y":
        task()
    else:
        print(f" \n{task} - Skipped")
print("\n ---THE END---")
