from handler.execute_option import execute_option

def main_loop():
    menu_loop = True
    
    while menu_loop:
        correct_option = False
        while not correct_option:
            print("\nSelecciona una opcion:\n")
            print("1. Agregar tarea")
            print("2. Editar tarea")
            print("3. Marcar como realizada")
            print("4. Borrar tarea")
            print("5. Listar tareas")
            print("6. Salir")
            try:
                option = int(input("\nPor favor ingresa la opcion a realizar: "))
                
                if option < 1 or option > 6:
                    print("\nPorfavor ingresa una de las opciones disponibles\n")
                elif option == 6:
                    print("\nGracias por usar el programa")
                    menu_loop = False
                    break
                else:
                    execute_option(option)
                    correct_option = True
            except ValueError:
                print("\nPorfavor ingresa un numero\n")



def run():
    main_loop()
    


if __name__ == "__main__":
    run()