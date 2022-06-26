from handler.execute_option import execute_option

def main():
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
                min_opt = 1
                max_opt = 6
                if option < min_opt or option > max_opt:
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
    


if __name__ == "__main__":
    main()