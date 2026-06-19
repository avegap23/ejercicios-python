# 50. Crear una agenda simple con diccionarios.

agenda = {}
cont_dias = 1

while cont_dias <= 5:
    input_dia = input(f"¿Asignar tareas al día {cont_dias}? [s/n]").lower()

    if input_dia == 's':
        dia = agenda[f"dia{cont_dias}"] = {}
        cont_tarea = 0
        input_continuar = 's'

        print(f"\nDía {cont_dias}:")
        while input_continuar == 's':
            cont_tarea += 1
            input_tarea = input("Introducir tarea...: ")
            dia[cont_tarea] = input_tarea
            input_continuar = input(f"¿Continuar asignando en el día {cont_dias}? [s/n]: ").lower()

            while input_continuar not in ['s', 'n']:
                print("Error: Introduce SÓLO [s]í o [n]o")
                input_continuar = input(f"¿Continuar asignando en el día {cont_dias}? [s/n]: ").lower()
        
        cont_dias += 1
        print('\n')

    elif input_dia == 'n':
        cont_dias += 1
        continue
    
    else:
        print("\nError: Introduce SÓLO [s]í o [n]o")
        continue

print(agenda)