from handler.create_task import create_task


def add_task():
    
    task = create_task()
    task.print_task(1)