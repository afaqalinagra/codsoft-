import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        # Creation of the  GUI elements:-
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.edit_button = tk.Button(root, text="Edit Task", command=self.edit_task)
        self.edit_button.grid(row=0, column=2, padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=0, column=3, padx=10, pady=10)

        self.clear_button = tk.Button(root, text="Clear All", command=self.clear_all)
        self.clear_button.grid(row=0, column=4, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

        # Loading the  tasks from a file :-
        self.load_tasks()

        # Binding the  double-click event to the listbox for updating tasks:-
        self.task_listbox.bind("<Double-Button-1>", self.update_task)

        # Set up of  the main loop:-
        root.mainloop()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            current_task = self.task_listbox.get(selected_task_index)
            new_task = simpledialog.askstring("Edit Task", "Edit task:", initialvalue=current_task)
            if new_task:
                self.tasks[selected_task_index[0]] = new_task
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(tk.END, new_task)
                self.save_tasks()

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.task_listbox.delete(selected_task_index)
            del self.tasks[selected_task_index[0]]
            self.save_tasks()

    def clear_all(self):
        self.task_listbox.delete(0, tk.END)
        self.tasks = []
        self.save_tasks()

    def update_task(self, event):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            current_task = self.task_listbox.get(selected_task_index)
            new_task = simpledialog.askstring("Update Task", "Update task:", initialvalue=current_task)
            if new_task:
                self.tasks[selected_task_index[0]] = new_task
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(tk.END, new_task)
                self.save_tasks()

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.read().splitlines()
                for task in tasks:
                    self.tasks.append(task)
                    self.task_listbox.insert(tk.END, task)
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
