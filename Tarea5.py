import sys

#Dejé esta para que sea mas facil probar cosas, pero hay que dejar la otra
def cargar_grafo(ruta: str)->list:
    archivo = open (ruta, "r")
    linea = archivo.readline()
    grafo = []
    while linea != "":
        lista = []
        for n in linea.split("\t"):
            lista.append(int(n))
        grafo.append(lista)
        linea = archivo.readline()

    archivo.close()
    return grafo

#Esta es la que recibe por entrada estandar por consola
def cargar_grafo_entrada_estandar()->list:
    linea = sys.stdin.readline()
    grafo = []
    while linea != "":
        lista = []
        for n in linea.split("\t"):
            lista.append(int(n))
        grafo.append(lista)
        linea = sys.stdin.readline()

    return grafo