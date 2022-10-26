import java.util.ArrayList;
import java.util.PriorityQueue;

class Dalgo{

    


public int[] dijkistra( int inicio, int maxvertices, Object[][] matrix) {
     int[] distancia = new int[maxvertices+1];
     int[] padre = new int[maxvertices+1];
     boolean[] visto = new boolean[maxvertices+1];
     for (int i = 1; i < maxvertices+1; i++) {
         distancia[i] = 1200000000;
         padre[i] = -1;
        visto[i] = false;
     }
     distancia[inicio]=0;
     PriorityQueue<Integer> pila = new PriorityQueue<>();
     pila.add(distancia[inicio]+1);
     while (!pila.isEmpty()) {
        int u = pila.poll();
        visto[u] = true;

     for (int i = 1; i < maxvertices+1; i++) { 
         if ( (Integer)matrix[u][i] != 0) {
             if (distancia[i] > distancia[u] + (Integer)matrix[u][i]) {  
                distancia[i] = distancia[u] + (Integer)matrix[u][i];
                System.out.print("| "+matrix[u][i]+" u:"+u+" i:"+i);
                padre[i] = u;
                pila.add(i);
             }
         }
    }
 }
return distancia;
}

}