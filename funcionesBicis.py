import csv
import random
import json
nombre_archivo_csv = "bicicletas.csv"
#1)
def obtener_camino_archivo_actual(nombre_archivo_csv):
    """Obitnene el camino del archivo

    Args:
        nombre_archivo_csv (.csv): archivo tipo ".csv", contiene lista con bicicletas y subcategorias de las mismas

    Returns:
        lista_bicis(list): Lista de multiples dik, de bicicletas
    """
    if type(nombre_archivo_csv) is not str:
        raise TypeError("La ruta no es de tipo str")
    with open(nombre_archivo_csv, 'r', encoding="utf-8") as archivo:
        archivo = archivo.readlines()
        lista_bicis = []
        for linea in archivo:
            bici = {}
            linea = linea.strip("\n")
            categorias = linea.split(",")
            bici["id_bike"] = categorias[0]
            bici["nombre"] = categorias[1]
            bici["tipo"] = categorias[2]
            bici["tiempo"] = categorias[3]
            if bici["id_bike"].isdigit():
                lista_bicis.append(bici)
        print(lista_bicis)
        return lista_bicis
lista_bicis = obtener_camino_archivo_actual(nombre_archivo_csv) 

#3)
def poner_tiempo_aleatorio(lista_bicis:list):
    """Mapea cada tipo de bici y calculara aleatoriamente un valor de timepo(de entre 50 a 120)

    Args:
        lista_bicis (list): lista de diccionarios de bicicletas
    """
    for bici in lista_bicis:
        bici["tiempo"] = random.randint(50, 120)
        print(f"Bicicleta {bici["id_bike"]} ({bici["tipo"]}): {bici["tiempo"]} minutos")
poner_tiempo_aleatorio(lista_bicis)

#4)
def informar_ganador(lista_bicis:list):
    """Informa quien llegó primero, calculando el menor tiempo. Si hay empate, tambien lo informa 

    Args:
        lista_bicis (list): lista de diccionarios de bicicletas
    """
    if type(lista_bicis) is not list:
        raise TypeError("La lista no es del tipo")
    bandera_primer_elemento = True
    for el in lista_bicis:
        if bandera_primer_elemento == True or menor_tiempo["tiempo"] > el["tiempo"]:
            menor_tiempo = el
            bandera_primer_elemento = False
    ganadores = [bici for bici in lista_bicis if bici["tiempo"] == menor_tiempo["tiempo"]]
    if len(ganadores) == 1:
        print(f"El ganador es: {ganadores[0]["nombre"]} con un tiempo record de {menor_tiempo["tiempo"]} minutos.")
    else:
        print(f"Hubo un empate entre: {[ganador["nombre"] for ganador in ganadores]} con un tiempo record de {menor_tiempo["tiempo"]} minutos.")
informar_ganador(lista_bicis)

#5)
tipo_elegido = input("Elija el tipo de bici a filtrar: ")
def filtrar_por_tipo(lista_bicis:list, tipo_elegido):
    
    """Filtra una bicicleta elegida por el usuario, y escribira un archivo igual al original, solo con el genero seleccionado

    Args:
        lista_bicis (list): lista de diccionarios de bicicletas
        tipo (_type_): _description_

    Returns:
        tipo_elegido: Input que pide al usuario que tipo de bici quiere para que se filtre
    """
    tipo_elegido = input("Elije que bici quieres filtrar: ")
    
    bici_filtrada = [bici for bici in lista_bicis if bici['tipo'] == tipo_elegido]
    return bici_filtrada
bici_filtrada = filtrar_por_tipo(lista_bicis, tipo_elegido)


#6)
def calcular_promedio_por_tipo(lista_bicis):
    """Calcula el promedio de las bicis segun el tipo de las mismas

    Args:
        lista_bicis (list): lista de diccionarios de bicis

    """
    total_tiempo = {}
    cantidades = {}

    for bici in lista_bicis:
        tipo = bici["tipo"]
        tiempo = float(bici["tiempo"])

        if tipo not in total_tiempo:
            total_tiempo[tipo] = tiempo
            cantidades[tipo] = 1
        else:
            total_tiempo[tipo] += tiempo
            cantidades[tipo] += 1

    promedios = {}
    for tipo in total_tiempo:
        promedio = total_tiempo[tipo] / cantidades[tipo]
        promedios[tipo] = promedio

    return promedios
calcular_promedio_por_tipo(lista_bicis)

def lista_swap(lista_bicis: list, i: int, j: int):
    """Swap entre dos elementos
    Args:
        lista_bicis (list): lista de bicicletas
        i (int): el primer indice
        j (int): el segundo indice
    """
    aux = lista_bicis[i]
    lista_bicis[i] = lista_bicis[j]
    lista_bicis[j] = aux


def bici_ordenada_por_tipo (lista_bicis:list):
    """ordena las bicicletas por tipo
    Args:
        lista_bicis (list): lista de bicis
    """
    for i in range(0, len(lista_bicis)-1):
        for j in range(i +1, len(lista_bicis)):
                if float(lista_bicis[i]["tiempo"]) > float(lista_bicis[j]["tiempo"]):
                    lista_swap(lista_bicis, i, j)
bici_ordenada_por_tipo(lista_bicis)

#7)
def ordenar_bicicletas_de_manera_ascendente (lista_bicis:list):
    """Ordena las bicicletas por tipo de manera ascendente
    Args:
        lista_bicis (list): lista de bicis
    """
    if type(lista_bicis) != list:
        raise TypeError("La lista no es de tipo list")
    diccionario = {}
    for bicicleta in lista_bicis:
        bicicleta = bicicleta["tipo"]
        if bicicleta not in diccionario:
            diccionario[bicicleta] = [{"nombre":bicicleta["nombre"], "tipo":bicicleta["tipo"], "id_bike":bicicleta["id_bike"], "tiempo":bicicleta["tiempo"]}]

        else:
            diccionario[bicicleta].append({"nombre":bicicleta["nombre"], "tipo":bicicleta["tipo"], "id_bike":bicicleta["id_bike"], "tiempo":bicicleta["tiempo"]})
    lista_preparada = []
    for tipo in diccionario.keys():
        ordenar_bicicletas_de_manera_ascendente(diccionario[tipo])
        for bicicleta in diccionario[tipo]:
            lista_preparada.append(bicicleta)
    for participante in lista_preparada:
        print(f"{bicicleta["nombre"]}, {bicicleta['tiempo']}, {bicicleta['id_bike']}, {bicicleta['tipo']}")
    return lista_preparada
ordenar_bicicletas_de_manera_ascendente(lista_bicis)

#8)
def guardar_en_json( lista_bicis:list):
    """Guarda la lista en un archivo json
        lista_bicicleta (list): La lista de bicicleta
    """
    if type(lista_bicis) != list:
        raise TypeError("La lista no es de tipo list")
    archivo.json = {"bicicletas":lista_bicis}
    with open("w", encoding="utf-8") as archivo:
        json.dump(archivo.json, archivo, indent=4)
guardar_en_json(lista_bicis)











                    