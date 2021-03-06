import os
import random
import tkinter
from tkinter import messagebox

# root window
root = tkinter.Tk()


# classes
class Tasks:
    def __init__(self):
        # sample data for testing
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
            print("{} has been removed from the to do list.".format(task))
        else:
            print("That task is not in on your to do list.")

    def delete_task_number(self, task_number):
        if self.tasks[task_number] in self.tasks:
            self.tasks.remove(self.tasks[task_number])
        else:
            print("This task number is not on your to do list.")

    def delete_all_tasks(self):
        for _ in self.tasks:
            self.tasks.remove(_)
            print("All to dos have been deleted.")

    def reset_tasks(self, response):
        if response:
            self.tasks = []
        else:
            pass

    def print_tasks(self):
        for _ in range(0, len(self.tasks)):
            print(_, '|', self.tasks[_])


class Widgets:
    def __init__(self, master):
        self.master = master
        master.title("To Do Manager")
        self.bg = "#fff"
        self.text = 'Label'
        self.widget = ''
        self.width = 15
        self.fg = '#556B2F'
        master.geometry("405x340")

    def set_name(self, name, r, c):
        self.widget = tkinter.Label(self.master, text=name)
        self.widget.grid(row=r, column=c)

    def input_text(self):
        self.widget = tkinter.Entry(self.master, width=self.width)
        self.widget.grid(row=4, column=1)

    def display_button(self, txt, command, r, c):
        self.widget = tkinter.Button(root, text=txt, bg=self.bg, command=command)
        self.widget.grid(row=r, column=c)

    def to_do_box(self):
        self.widget = tkinter.Listbox(root)
        self.widget.grid(row=5, column=1, rowspan=6)

    def alert(self, title, message):
        self.widget = tkinter.messagebox.showwarning(title, message)


# functions
def print_menu():
    print("""
Todo List

Please enter a command:

A) Add a new task
B) Print the number of to dos
C) Search for a task
D) Delete a task by name
E) Delete a task by number
F) Sort to do list in ascending order
G) Sort to do list descending order
H) Print a random task
I) Reset to do list
__________________
__________________
M) Show the menu
P) Print to do list
Q) Quit the program
""")

    os.system("clear")


def add_to_do():
    # add_task = input("What task would you like to add? >")
    add_task = text_input.widget.get()
    if not add_task == "":
        to_do_list.add_new_task(add_task)
        text_input.widget.delete(0, 'end')
        clear_to_do_list()
        show_to_do_list()
    else:
        alert_text_input.alert('No Task Entered', 'Please enter a task')


def sort_asc():
    clear_to_do_list()
    to_do_list.tasks.sort()
    show_to_do_list()
    print("Your to do list has been sorted in ascending order.")


def sort_desc():
    clear_to_do_list()
    to_do_list.tasks.sort()
    to_do_list.tasks.reverse()
    show_to_do_list()
    print("Your to do list has been sorted in descending order.")


def random_choice():
    task = (random.choice(to_do_list.tasks))
    label_display.widget['text'] = task
    print(task)


def reset_tasks():
    # answer = input("Are you sure you want to reset the list. (Y)es or (N)o? >").upper()
    confirm = tkinter.messagebox.askyesno("Delete All To Dos", "Are you sure you wish to delete all to dos in the list?")
    to_do_list.reset_tasks(confirm)
    show_to_do_list()


def remove_by_name():
    # delete_task = input("What task would you want to remove?")
    # to_do_list.delete_task_name(delete_task)
    delete_task = list_box.widget.get('active')
    if delete_task in to_do_list.tasks:
        clear_to_do_list()
        to_do_list.delete_task_name(delete_task)
        show_to_do_list()


def remove_by_index():
    index = int(input("What task number do you want to remove?"))
    to_do_list.delete_task_number(index)


def search_to_dos():
    search_task = input("What task would you like to search for?")
    to_do_list.search_tasks(search_task)


def to_do_list_length():
    number_of_to_dos = len(to_do_list.tasks)
    msg = "Number of to dos to complete: {}".format(number_of_to_dos)
    task_number_display.widget['text'] = msg


def show_to_do_list():
    clear_to_do_list()
    for to_do in to_do_list.tasks:
        list_box.widget.insert("end", to_do)


def clear_to_do_list():
    list_box.widget.delete(0, "end")


# class instances
to_do_list = Tasks()
label_title = Widgets(root)
label_display = Widgets(root)
task_number_display = Widgets(root)
text_input = Widgets(root)
btn_add_task = Widgets(root)
btn_shows_tasks = Widgets(root)
btn_delete_all = Widgets(root)
btn_delete_one = Widgets(root)
btn_sort_asc = Widgets(root)
btn_sort_desc = Widgets(root)
btn_choose_random = Widgets(root)
btn_number_of_to_dos = Widgets(root)
btn_reset_tasks = Widgets(root)
btn_exit = Widgets(root)
list_box = Widgets(root)
alert_text_input = Widgets(root)
delete_confirmation_message = Widgets(root)

# widgets
label_title.set_name('To do List', 1, 0)
task_number_display.set_name('', 2, 1)
text_input.input_text()
btn_shows_tasks.display_button("Show all to dos", show_to_do_list, 2, 0)
btn_add_task.display_button("Add new to do", add_to_do, 4, 0)
# btn_delete_all.display_button('Delete all to dos', to_do_list.delete_all_tasks)
btn_delete_one.display_button('Delete to do', remove_by_name, 5, 0)
btn_sort_asc.display_button('Sort tasks (asc)', sort_asc, 6, 0)
btn_sort_desc.display_button('Sort tasks (desc', sort_desc, 7, 0)
btn_choose_random.display_button('Choose random to do', random_choice, 8, 0)
btn_number_of_to_dos.display_button('Number of to dos', to_do_list_length, 9, 0)
btn_reset_tasks.display_button('Delete All Todos', reset_tasks, 11, 0)
btn_exit.display_button('Exit', exit, 12, 0)
label_display.set_name('', 3, 1)
list_box.to_do_box()


# main loop
# functions to run on start up
show_to_do_list()
root.mainloop()
print_list_to_console = False


# main loop
while print_list_to_console:
    print_menu()
    choice = input("\n> ").upper()

    if choice == "A":
        add_to_do()
    elif choice == "B":
        to_do_list_length()
    elif choice == "C":
        search_to_dos()
    elif choice == "D":
        remove_by_name()
    elif choice == "E":
        remove_by_index()
    elif choice == "F":
        sort_asc()
    elif choice == "G":
        sort_desc()
    elif choice == "H":
        random_choice()
    elif choice == "I":
        reset_tasks()
    elif choice == "M":
        print_menu()
    elif choice == "P":
        to_do_list.print_tasks()
    elif choice == "Q":
        break

    else:
        print("Your choice was not recognised. Please try again.")

    delay = input("\nPress ENTER to continue.")

