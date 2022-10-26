from operator import sub


matriz = [[-1 ,-1, -1, 1, -1, -1, -1],
           [-1, -1, -1, -1, -1, 1, -1 ],
           [-1, -1, -1, 1, -1, -1, -1] ,
           [1, -1, 1, -1, -1, -1, -1] ,
           [-1, -1, -1, -1, -1, -1, 1] ,
           [-1, 1, -1, -1, -1, -1, -1] ,
           [-1, -1, -1, -1, 1, -1, -1] ,
            ]




def bfsOfGraph(V, adj):
 
    bfs_traversal = []
    vis = [False]*V
    for i in range(V):
 
        # To check if already visited
        if (vis[i] == False):
            q = []
            vis[i] = True
            q.append(i)
 
            # BFS starting from ith node
            while (len(q) > 0):
                g_node = q.pop(0)
 
                bfs_traversal.append(g_node)
                for it in adj[g_node]:
                    if (vis[it] == False):
                        vis[it] = True
                        q.append(it)
 
    return bfs_traversal


"""def BDF(matriz):
    visitados = []
    rta = []
    for k in range(0,len(matriz[0])):
        for i in range(0,len(matriz[0])):
            n = matriz[k][i]
            if n == 1 and (i not in visitados):
                subconjunto = [k]
                if n == 1:
                    subconjunto.append(i)
                    for j in range(0,len(matriz[0])):
                        m = matriz[i][j]
                        if m == 1 and j not in subconjunto:
                            subconjunto.append(j)
                rta.append(subconjunto)            
                        
                    
            visitados.append(i)
        
    return None"""

"""def BDF2(matriz):
    largo = len(matriz[0])
    conjuntos = []
    rta = []
    
    for i in range(0,largo):
        for j in range(0,largo):
            n = matriz[i][j]
            if n == 1:
                conjuntos.append([i, j])

    for i in range(0,len(conjuntos)):
        for j in range(0,len(conjuntos)):
            print(conjuntos[i][0])
            if i != j and conjuntos[i][0] in conjuntos[j] and conjuntos[i][1]  in conjuntos[j]:
                conjuntos.pop(j)
                
                

    print(conjuntos)"""
    


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


a = subconjuntos(matriz)
print(a)