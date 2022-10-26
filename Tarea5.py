import sys

def cargar_grafo()->list:
    linea = sys.stdin.readline()
    grafo = []
    while linea != "":
        lista = []
        for n in linea.split("\t"):
            lista.append(int(n))
        grafo.append(lista)
        linea = sys.stdin.readline()
    return grafo

print(cargar_grafo())


