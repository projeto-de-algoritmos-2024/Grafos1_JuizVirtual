from typing import List
# vi as tags do exercicio, e vi que ele tem tambem union find, entao tive de estudar esse tipo de 
# estrutura para executar a questao
# descobri que para criar uma classe, o que sera necessario para fazer uma union find, eu preciso
# criar uma instancia do mesmo, estava pesquisando sobre union find e nao estava entendo o que
# eram os nomes precedidos por __, vi que serviam exatamente para esse proposito
# usarei o que melhor entendi durante a pesquisa aqui no coigo antes de fazer minha solucao,
# que foi o Union by size do site https://www.geeksforgeeks.org/introduction-to-disjoint-set-data-structure-or-union-find-algorithm/

class UnionFind:
    def __init__(self,n):
        # a partir disso criamos os vetores para os caminhos que apenas um dos lados podem percorrer
        self.parent = list(range(n))

        # inicia o vetor de tamanho em 1

        self.Size = [1] * n

    # funcao find usada para identificar o no principal ou raiz para o vetor que possuir o caminho i

    def find(self,i) :
        if self.parent[i] != i:
            # aqui o algoritmo fornecido causa uma supressao do caminho, tornando i o pai do vetor,
            # pelo que entendi, e necessario para funcionar o UnionFind
            self.parent[i] = self.find(self.parent[i])
            return self.parent[i]
    # agora e a funcao de uniao por tamanho, nesse caso, a uniao obedece que o vetor menor sera incorporado
    # no vetor maior, e o vetor maior aumentara seu tamanho igual ao numero de elementos do menor,
    # se os tamanhos forem iguais, nao importa a ordem de uniao

    def UnionBySize(self, i, j) :
       # encontra os nos pais dos vetores i e j
        irep = self.find[i]

        jrep = self.find[j]

        # terceira condicao(tamanhos iguais)
        if irep == jrep :
            return
        # pegando o tamanho dos vetores
        isize = self.Size[irep]
        jsize = self.Size[jrep]

        # condicao de uniao agora
        if isize < jsize :
            # move o vetor(descobri que chamam de arvore so agora, vou continuar com vetor)i para o vetor j
            self.parent[irep] = jrep

            # aumenta o tamanho do vetor j em i
            self.Size[jrep] += self.Size[irep]
        # caso seja o contrario
        else :
            self.parent[jrep] = irep
            self.Size[irep] += self.Size[jrep]

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # com a criacao o UnionFind, preciso apenas criar o vetor deste tipo para Alice e Bob e dai 
        # continuar a questao utilizando find e union quando necessario
         caminhoA = UnionFind(n)
         caminhoB = UnionFind(n)
         