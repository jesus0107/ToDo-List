class Task:
    def __init__(self, task, date, done):
        self.task =  task
        self.date = date
        self.done = done

    def print_task(self, index):
        print_task = "{0} -- Tarea: {1} -- Fecha limite: {2} -- Realizado: {3}"
        print(print_task.format(index, self.task, self.date, self.done))