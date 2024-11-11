from collections import deque # biblioteca para usar listas como filas
from typing import List 
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
       # segunda tentativa, nao mudei a logica, mas tentarei usar um tipo de estrutura
       # que achei na documentacao chamado set, como se fosse um vetor, nao entendi direito a estrutura,
       # porem nao acho que um vetor usual ja funcionaria aqui
        grafo = set()

        for i in range(n) :
            grafo.add(i)
        # nao consegui tentando fazer com booleano, vou tentar usando o comando remove que achei na documentacao do python
        # em data structures
        for edge in edges :
            # edges e composto por 2 entradas, so estava citando uma na primeira tentativa, vou tentar colocar separado aqui
            de = edge[0]
            para = edge[1]
            if para in grafo :
                grafo.remove(para)
        return List(grafo)
