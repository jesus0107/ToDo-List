from handler.add_task import add_task
from handler.print_data_list import print_data_list
from DB.connection import DAO

add = 1
edit_update = 2
done = 3
delete = 4
show = 5

def execute_option(option):
    dao = DAO()
    try:
        if option == add:
            add_task()
        elif option == edit_update:
            pass
        elif option == done:
            pass
        elif option == delete:
            pass
        elif option == show:
            data_list = dao.print_task_list()
            print_data_list(data_list)
    except Exception as err:
        print("Ocurrio un error: ", err)
    