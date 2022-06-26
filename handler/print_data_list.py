def print_data_list(data_list):
    if len(data_list) > 0:
        for item in data_list:
            print(f"{item[0]} -- Tarea: {item[1]} -- Fecha limite: {item[2]} -- Realizado: {item[3]}")
    else:
        print("No se encontraron cursos")