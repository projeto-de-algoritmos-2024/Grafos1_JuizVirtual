#include <stdio.h>
#include <stdlib.h>

#define UNVISITED 0
#define VISITING 1
#define VISITED 2

int dfs(int* edges, int* status, int node, int step) {
    if (status[node] == step) {
        return step - status[node];  
    }
    if (status[node] > 0 || edges[node] == -1) {
        return -1;  
    }
    status[node] = step;  
    int cycleLength = dfs(edges, status, edges[node], step + 1);  
    status[node] = -1;  

    return cycleLength;
}

int longestCycle(int* edges, int edgesSize) {
    int *status = (int*) calloc(edgesSize, sizeof(int));  
    int longestCycleLength = -1;  

    for (int i = 0; i < edgesSize; i++) {
        if (status[i] == UNVISITED) {  
            int cycleLength = dfs(edges, status, i, 1);  
            if (cycleLength > longestCycleLength) {
                longestCycleLength = cycleLength;  
            }
        }
    }

    free(status);  
    return longestCycleLength;
}
