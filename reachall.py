from collections import deque # biblioteca para usar listas como filas
from typing import List 
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # tentativa que vejo como gambiarra: transformar a lista de booleanos em um dicionario, pelo que vi
        # na documentacao, ele e usado quando se precisa de chaves, nao sei se vai bastar para corrigir a 
        # falha no leetcode, mas vou tentar.
        
        caminho = {}
        
        for i in range(n):
            
            caminho[i] = False
           
            # o problema pede que seja entregue os nos que nao possuem caminhos direcionados a ele, como e um par ordenado
            # decidi por usar um vetor de booleanos inicializado como falso, representando que nao existem caminhos
            # de forma que a solucao devera trazer exatamente os que nao sao acessiveis como resposta, pois e o que
            # ocorre nos exemplos entregues pelo exercicio
        
        # usando a documentacao do proprio python, ele me traz o for de C como range ao meu ver, e o for para mim e mais 
        # para trabalhar em cima de uma variavel ja entregue, nesse caso a lista encadeada edges entregue pela funcao 

        for aresta in edges :
            # criando as variaveis from e to que aparecem no problema
            
            x,y = aresta
            
            # como x e o from, ele sempre tera uma direcao a partir dele, ou seja, todos os y, que sao to, podem ou nao atingir 
            # todos os outros vertices, entao todos os vertices que aparecerem em y devem ser colocados como verdadeiro
            # pois assim apenas os que nao possuem caminho ate si serao salvos, e eles sao a resposta

            caminho[y] = True
        
        # agora criamos o retorno da funcao, onde todos que tiverem permanecido com o valor falso serao copiados para o mesmo,
        # usando fila, por isso importei a biblioteca indicada na documentacao de Python deque

        resposta = []

        for vert in range(n) :
            if not caminho[vert]:
                resposta.append[vert]
        return resposta