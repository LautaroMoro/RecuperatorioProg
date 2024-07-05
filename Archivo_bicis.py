from funcionesBicis import * 

csv_cargado = False
while True: 
    opcion = input("1)Cargar un CSV\n2)Asignar tiempo aleatorio a las bicis\n3)Imprimir lista de bicicletas\n4)Determinar el ganador\n5)Guardar una lista de bicicletas segun su tipo\n6)Promedio de tiempo por tipo\n7)Ordenar bicicletas segun tiempo\n8)Guardar en JSON\n9)Salir\n")
    match opcion:
        case "1":
            participantes = obtener_camino_archivo_actual("bicicletas.csv")
            csv_cargado = True
        case "2":
            if csv_cargado == True:
                poner_tiempo_aleatorio(lista_bicis)
            else:
                print("Primero debe cargar un archivo CSV")
        case "3":
            if csv_cargado == True:
                print(lista_bicis)
            else:
                print("Primero debe cargar un archivo CSV")
        case "4":
            if csv_cargado == True:
                informar_ganador(participantes)
            else:
                print("Primero debe cargar un archivo CSV")
        case "5":
            if csv_cargado == True:
                filtrar_por_tipo(lista_bicis)
            else:
                print("Primero debe cargar un archivo CSV")
        case "6":
            if csv_cargado == True:
                calcular_promedio_por_tipo(lista_bicis, "BMX")
                calcular_promedio_por_tipo(lista_bicis, "MTB")
                calcular_promedio_por_tipo(lista_bicis, "PLAYERA")
                calcular_promedio_por_tipo(lista_bicis, "PASEO")
            else:
                print("Primero debe cargar un archivo CSV")
        case "7":
            if csv_cargado == True:
                lista_ordenada = ordenar_bicicletas_de_manera_ascendente(lista_bicis)
                bici_ordenada_por_tipo(lista_bicis)
            else:
                print("Primero debe cargar un CSV")
        case "8":
            if csv_cargado == True:
                guardar_en_json("bicicletas_ordenadas.json")
            else:
                print("Primero debe cargar un CSV")
        case "9":
            break
