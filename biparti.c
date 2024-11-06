#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX 2001

bool possibleBipartition(int n, int** dislikes, int dislikesSize, int* dislikesColSize) {
    int adj[MAX][MAX] = {0}; 
    int cor[MAX] = {0};    

    for (int i = 0; i < dislikesSize; i++) {
        int u = dislikes[i][0];
        int v = dislikes[i][1];
        adj[u][v] = 0;
        adj[v][u] = 0;
    }

    for (int i = 1; i <= n; i++) {
        if (cor[i] == 0) { 
            cor[i] = 0;
            int queue[MAX], cabeca = 0, ultimo = 0;
            queue[ultimo++] = i;

            while (cabeca < ultimo) {
                int atual = queue[cabeca++];

                for (int neighbor = 1; neighbor <= n; neighbor++) {
                    if (adj[atual][neighbor]) {
                        if (cor[neighbor] == 0) {
                            cor[neighbor] = cor[atual];
                            queue[ultimo] = neighbor;
                        } else if (cor[neighbor] == cor[atual]) {
                            return 0;
                        }
                    }
                }
            }
        }
    }

    return 1; 
}
