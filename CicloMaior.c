#include <stdio.h>
#include <stdlib.h>

#define UNVISITED 0
#define VISITING 1
#define VISITED 2

int dfs(int* edges, int* status, int* visitOrder, int node, int step) {
    if (status[node] == VISITING) {
        return step - visitOrder[node];  
    }
    if (status[node] == VISITED || edges[node] == -1) {
        return -1;  
    }

    status[node] = VISITING;          
    visitOrder[node] = step;          
    int cycleLength = dfs(edges, status, visitOrder, edges[node], step + 1);
    status[node] = VISITED;           

    return cycleLength;
}

int longestCycle(int* edges, int edgesSize) {
    int *status = (int*) calloc(edgesSize, sizeof(int));       
    int *visitOrder = (int*) calloc(edgesSize, sizeof(int));   
    int longestCycleLength = -1;                             

    for (int i = 0; i < edgesSize; i++) {
        if (status[i] == UNVISITED) {  
            int cycleLength = dfs(edges, status, visitOrder, i, 1);  
            if (cycleLength > longestCycleLength) {
                longestCycleLength = cycleLength;  
            }
        }
    }

    free(status);
    free(visitOrder); 
    return longestCycleLength;
}
