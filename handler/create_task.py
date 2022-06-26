from datetime import date
from unicodedata import name


class Task:
    def __init__(self, task, date, done = False):
        self.task =  task
        self.date = date
        self.done = done

    def print_task(self, index):
        print_task = "{0} -- Tarea: {1} -- Fecha limite: {2} -- Realizado: {3}"
        print(print_task.format(index, self.task, self.date, self.done))


def create_task():
    task_name = input("Tarea a realizar: ")
    task_date = input("Porfavor ingresa la fecha limite para la tarea: ")
    
    task = Task(task_name, task_date)
    return task