from typing import List
# vi as tags do exercicio, e vi que ele tem tambem union find, entao tive de estudar esse tipo de 
# estrutura para executar a questao
# descobri que para criar uma classe, o que sera necessario para fazer uma union find, eu preciso
# criar uma instancia do mesmo, estava pesquisando sobre union find e nao estava entendo o que
# eram os nomes precedidos por __, vi que serviam exatamente para esse proposito
# usarei o que me parece o certo para solucionar o problema, que e por ranqueamento, usarei um UnionFind 
# que encontrei que facilita de fazer o exercicio colocando o retorno do Union como 0 ou 1, possibilitando
# o uso de um contador na solucao
class UnionFind:
    def __init__(self,n):
        self.n = n
        self.parent = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)
    
    def find(self, x) :
        while x != self.parent[x] :
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def Union(self, x, y) :
        p1,p2 = self.find(x), self.find(y)
        if p1 == p2 :
            return 0
        if self.rank[p1] > self.rank[p2] :
            self.rank[p1] += self.rank[p2]
            self.parent[p2] = p1
        else :
            self.rank[p2] += self.rank[p1]
            self.parent[p1] = p2
        self.n -= 1
        return 1
    def isConnected(self) :
        return self.n <= 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # com a criacao o UnionFind, preciso apenas criar o vetor deste tipo para Alice e Bob e dai 
        # continuar a questao utilizando find e union quando necessario
         caminhoA = UnionFind(n)
         caminhoB = UnionFind(n)
         arestasI = 0 # esse e o contador de arestas que precisamos manter no grafo
        # nao sao nomes significativos a priori, mas t e para o tipo de aresta ou caminho,
        # i  e para onde ele se inicia e o refere-se ao objetivo do caminho
         