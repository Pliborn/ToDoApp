import tkinter as tk
import json

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("300x400")
        
        # Закрепляем окно поверх всех других окон
        self.root.wm_attributes("-topmost", 1)  

        self.tasks = []
        self.load_tasks()

        # Добавление элементов интерфейса
        self.task_entry = tk.Entry(root)
        self.task_entry.pack(pady=10)

        self.category_var = tk.StringVar(root)
        self.category_var.set("Выберите категорию")
        categories = ["Работа", "Учеба", "Личное"]
        self.category_menu = tk.OptionMenu(root, self.category_var, *categories)
        self.category_menu.pack(pady=10)

        self.add_button = tk.Button(root, text="Добавить задачу", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_list = tk.Listbox(root)
        self.task_list.pack(fill=tk.BOTH, expand=True, pady=10)

        self.update_task_list()

    def add_task(self):
        task = self.task_entry.get()
        category = self.category_var.get()
        if task and category != "Выберите категорию":
            self.tasks.append({"task": task, "category": category})
            self.update_task_list()
            self.save_tasks()

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, f"{task['task']} - {task['category']}")

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open("tasks.json", "w") as f:
            json.dump(self.tasks, f)

root = tk.Tk()
app = ToDoApp(root)
root.mainloop()
