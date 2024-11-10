#include <stdio.h>
#include <stdlib.h>

/** analise da funcao fornecida pelo leetcode:
 * n sao os vertices ou nos
 * edges e a matriz que indica a direcao de uma aresta
 * edgesSize acho que e a distancia entre arestas
 * edgesColSize acho que e o vetor que armazena as direcoes
 * returnSize acredito que seja o retorno do exercicio
 * Note: The returned array must be malloced, assume caller calls free().
 */



int* findSmallestSetOfVertices(int n, int** edges, int edgesSize, int* edgesColSize, int* returnSize) {
    int encaminha[edgesSize]; //salva se o vetor edges naquela posição mostra um caminho ou nao 
    int resposta[n]; // salva os vertices sem caminhos que chegam nele
    
    for(int i = 0; i <= n; i++){
        edgesColSize[i] = encaminha[i]++;
        }
    for(int i = 0; i <= n; i++){
        if(encaminha[i] == 0){
            resposta[i] = (int) edges[i];
        }
        returnSize[i] = resposta[i];
    }
    
    return returnSize;
}
