import os
import random


# classes
class Tasks:
    def __init__(self):
        self.tasks = ["Shopping", "Tidy room", "Buy milk", "Pack bag", "Check finances"]

    def add_new_task(self, new_task):
        self.tasks.append(new_task)
        print("New task has been added")

    def search_tasks(self, task):
        if task in self.tasks:
            print("{} is on the todo list.".format(task))
        else:
            print("{} is not on the todo list.".format(task))

    def delete_task_name(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("{} has been removed from the to do list.".format(delete))
        else:
            print("That task is not in on your to do list.")

    def delete_task_number(self, task_number):
        if self.tasks[task_number] in self.tasks:
            self.tasks.remove(self.tasks[task_number])
        else:
            print("This task number is not on your to do list.")

    def reset_tasks(self, response):
        if response == "Y":
            self.tasks = []
        elif response == "N":
            pass

    def print_tasks(self):
        for _ in range(0, len(self.tasks)):
            print(_, '|', self.tasks[_])


# functions
def print_menu():
    print("""
Todo List

Please enter a command:

A) Add a new task
B) Print the number of todos
C) Search for a task
D) Delete a task by name
E) Delete a task by number
F) Sort to do list in ascending order
G) Sort to do list descending order
H) Print a random task
I) Reset to do list

M) Show the menu
P) Print to do list
Q) Quit the program
""")

    os.system("clear")


# class instances
to_do_list = Tasks()

# main loop
while True:
    print_menu()
    choice = input("\n> ").upper()

    if choice == "A":
        add_task = input("What task would you like to add? >").upper()
        to_do_list.add_new_task(add_task)

    elif choice == "B":
        print(len(to_do_list.tasks))

    elif choice == "C":
        search_task = input("What task would you like to search for?").upper()
        to_do_list.search_tasks(search_task)

    elif choice == "D":
        delete_task = input("What task would you want to remove?").upper()
        to_do_list.delete_task_name(delete_task)

    elif choice == "E":
        index = int(input("What task number do you want to remove?"))
        to_do_list.delete_task_number(index)

    elif choice == "F":
        to_do_list.tasks.sort()
        print("Your to do list has been sorted in ascending order.")

    elif choice == "G":
        to_do_list.tasks.sort()
        to_do_list.tasks.reverse()
        print("Your to do list has been sorted in descending order.")

    elif choice == "H":
        print(random.choice(to_do_list.tasks))

    elif choice == "I":
        answer = input("Are you sure you want to reset the list. (Y)es or (N)o? >").upper()
        to_do_list.reset_tasks(answer)

    elif choice == "M":
        print_menu()

    elif choice == "P":
        to_do_list.print_tasks()

    elif choice == "Q":
        break

    else:
        print("Your choice was not recognised. Please try again.")

    delay = input("\nPress ENTER to continue.")
