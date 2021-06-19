# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import networkx as nx

while True:
    print("**************************************")
    print("        Algoritmos de grafos          ")
    print("**************************************")
    print("           MENU PRINCIPAL             ")
    print("**************************************")
    print("1 - Criar um Grafo")
    print("2 - Exibir um Grafo")
    print("3 - Finalizar o Programa")
    
    opt = int(input("Escolha uma opção: "))
    
    if opt == 1:
    
        i = 1
        vertice_list = []
        arestas_list = []
        
        qtd_vertice = int(input("Quantos vértices terá o grafo? "))
        
        for j in range(1,qtd_vertice+1):
            vertice_list.append(j)
            
        qtd_aresta = int(input("Quantas arestas terá o grafo? "))
        
        while i <= qtd_aresta:
            aresta_num1 = int(input("Informe o primeiro número da aresta: "))
            aresta_num2 = int(input("Informe o segundo número da aresta: "))
            tupla = (aresta_num1,aresta_num2)
            arestas_list.append(tupla)
            i+=1
            
        G = nx.Graph()
        G.add_nodes_from(vertice_list)
        G.add_edges_from(arestas_list)
        print("Grafo criado com sucesso!")
            
    elif opt == 2:
        try:
            nx.draw(G)
            plt.show()
        except NameError:
            print("Nenhum grafo encontrado")

    elif opt ==3:
        break
    else:
        print("Escolha uma opção válida.")
        continue
print("\nPrograma finalizado.")