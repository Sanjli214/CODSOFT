import tkinter as tk
from tkinter import messagebox

class SimpleToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple To-Do List")

        # List to store tasks
        self.tasks = []

        # Entry widget to input new tasks
        self.task_entry = tk.Entry(root, width=35)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Add Task button
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(root, height=10, width=50)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Update Task button
        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.grid(row=2, column=0, padx=10, pady=10)

        # Delete Task button
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)  # Clear the entry after adding task
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty")

    def update_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]  # Get index of selected task
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[selected_task_index] = new_task
                self.update_task_listbox()
                self.task_entry.delete(0, tk.END)  # Clear the entry after updating task
            else:
                messagebox.showwarning("Input Error", "Updated task cannot be empty")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to update")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]  # Get index of selected task
            del self.tasks[selected_task_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)  # Clear the Listbox
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)  # Add all tasks back to Listbox

# Running the application
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleToDoApp(root)
    root.mainloop()
