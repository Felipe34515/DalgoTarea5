


#dijkstra           
def dijkstra(grafo, vinicio):

    listainstancias = [float("inf") for _ in range(len(grafo))]
    v_visitados = [False for _ in range(len(grafo))]
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
   

#hacer for
#Parte1 = dijkstra(matrix,0)

#floydWarshall
INF = 1000000000
matriz = [
					[  0,   1, 3, INF],
					[  1,   0, 1, INF],
					[  3,   1, 0,   2],
					[INF, INF, 2,   0]
					]

def floyd_warshall(vertice, matriz):
	for k in range(0, vertice):
		for i in range(0, vertice):
			for j in range(0, vertice):
				matriz[i][j] = min(matriz[i][j], matriz[i][k] + matriz[k][j])


Parte2 = floyd_warshall(4, matriz)






felipe = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]]




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

Parte3 = bellman_ford(felipe,0)

print(Parte3)
