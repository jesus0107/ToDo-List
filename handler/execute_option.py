from handler.create_task import create_task

def execute_option(option):
    if option == 1:
        task = create_task()
        task.print_task(1)