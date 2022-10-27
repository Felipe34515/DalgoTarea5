from operator import sub
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
    
matriz = cargar_grafo()


def subconjuntos (matriz):
    rta = []
    max = 0
    rtaM = crearMatriz(matriz)
    for i in range(0, len(rtaM)):
        for j in range(0, len(rtaM)):
            if rtaM[i][j] > max:
                max = rtaM[i][j] 
    for i in range(0, max):
        rta.append([])
    #print(rtaM)
    for i in range(0, len(rtaM)):
        for j in range(0, len(rtaM)):
            for k in range(1, max+1):
                if k == rtaM[i][j]:
                    #print( i, rta[k-1] )
                    if i not in (rta[k-1]):
                        (rta[k-1]).append(i)
                    if j not in (rta[k-1]):
                        (rta[k-1]).append(j)
    return  rta

def crearMatriz(matriz):
    largo = len(matriz[0])
    visitados = []
    rtaM = []
    #print("\n" , rtaM , "\n")
    nSubconjuntos = 1
    
    for i in range(0, largo):
        rtaM.append([])
        for j in range(0, largo):
                rtaM[i].append(0)
    for i in range(0, largo):
        for j in range(0, largo):
            v = matriz[i][j]
            
            if v == 1 and ((i not in visitados) and (j not in visitados)):
                #print(visitados)
                visitados.append(i)
                visitados.append(j)
                rtaM[i][j] = nSubconjuntos
                rtaM[j][i] = nSubconjuntos
                #funcion verificar si hay más
                rtaM = verificar(matriz, rtaM, j, nSubconjuntos)
                nSubconjuntos = nSubconjuntos + 1
                # verificar si hay más subconjuntos
    return rtaM

def verificar(matriz, rtaM, columna_verificar, nSubconjuntos):
    largo = len(rtaM[0])
    for i in range(0, largo):
        v = matriz[i][columna_verificar]
        if v == 1:
            rtaM[i][columna_verificar] = nSubconjuntos
            rtaM[columna_verificar][i] = nSubconjuntos
    return rtaM 


respuesta = subconjuntos(matriz)
print(respuesta)