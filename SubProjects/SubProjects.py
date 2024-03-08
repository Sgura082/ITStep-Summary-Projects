import re

# --------------------TASK DESCRIPTIONS-------------------------------
# ------Task1: Calculator
# ------Task2:
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
Task01 = Task("x")
def task1_body():
    pass
    # ----------------Task Variables----------------------------------
    operations = {"+": lambda x,y: x+y,
                  }
    # ----------------Task Classes------------------------------------
    # ----------------Task Functions----------------------------------
    # ----------------Task BODY---------------------------------------
Task01.write_function(task1_body)

Task02 = Task("x")
def task2_body():
    pass
    # ----------------Task Variables----------------------------------
    # ----------------Task Classes------------------------------------
    # ----------------Task Functions----------------------------------
    # ----------------Task BODY---------------------------------------
Task02.write_function(task2_body)

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
