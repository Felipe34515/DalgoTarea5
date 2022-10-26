import time 
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

grafo=(cargar_grafo("distances5.txt"))


matriz = [[  0,   1, 3, 1],
		  [  1,   0, 1, 1],
		  [  3,   1, 0,   2],
		  [1, 1, 2,   0]
					]
#dijkstra           
def dijkstra(grafo, vinicio):

    listainstancias = [float("inf") for x in range(len(grafo))]
    v_visitados = [False for x in range(len(grafo))]
    listainstancias[vinicio] = 0
    while True:

        distancia_corta = float("inf")
        indice_corto = -1
        for i in range(len(grafo)):
           
            if listainstancias[i] < distancia_corta and not v_visitados[i]:
                distancia_corta = listainstancias[i]
                indice_corto = i

        if indice_corto == -1:
            return listainstancias

      
        for i in range(len(grafo[indice_corto])):
          
            if grafo[indice_corto][i] != 0 and listainstancias[i] > listainstancias[indice_corto] + grafo[indice_corto][i]:
                listainstancias[i] = listainstancias[indice_corto] + grafo[indice_corto][i]
        
        v_visitados[indice_corto] = True
   

def dijkstraCompleto(grafo):
    lista=[]
    for x in range(0,len(grafo)):
        lista.append(dijkstra(grafo,x))
    return lista

#floydWarshall


INF = 99999
def floydWarshall(n,graph): #n=no. of vertex
    dist=graph
    for k in range(n):
        for i in range(n):
            for j in range(n): 
                dist[i][j] = min(dist[i][j] ,dist[i][k]+ dist[k][j])
    return dist


def bellman_ford(matrix, source):
   
    
    n, inf = len(matrix), float("inf")
    v = range(n)

    dist = [inf for _ in v]
    dist[source] = 0
    
    for _ in range(n - 1):
        for i in v:
            for j in v:
                w = matrix[i][j]
             
                if dist[i] != inf and dist[i] + w < dist[j]:
                    dist[j] = dist[i] + w
                    
    for i in v:
        for j in v:
            w = matrix[i][j]
            if dist[i] != inf and dist[i] + w < dist[j]:
                return None
            
    return dist

def bellman_fordCompleto(grafo):
    lista=[]
    for x in range(0,len(grafo)):
        lista.append(bellman_ford(grafo,x))
    return lista

st=time.time()
Parte1 = dijkstraCompleto(grafo)
et=time.time()
elapsed_time = et - st
print('Execution time dijkstra:', elapsed_time*1000, 'Miliseconds')
#print(Parte1)

st=time.time()
Parte2 = floydWarshall(len(grafo), grafo)
et=time.time()
elapsed_time = et - st
print('Execution time floydWarshall:', elapsed_time*1000, 'Miliseconds')
#print(Parte2)

st=time.time()
Parte3 = bellman_fordCompleto(grafo)
et=time.time()
elapsed_time = et - st
print('Execution time bellman_ford:', elapsed_time*1000, 'Miliseconds')
#print(Parte3)