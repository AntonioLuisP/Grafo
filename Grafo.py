import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np
from collections import defaultdict 

class Grafo:

  def __init__(self, tipo, arestas, vertices):
    self.dirigido = tipo
    self.arestas = arestas
    self.vertices = vertices
    self.geraMatriz(vertices)

  def geraMatriz(self, vertices):
    qtd = len(vertices)
    self.tamanho = qtd
    self.matriz = pd.DataFrame((np.zeros((qtd, qtd))), index=vertices, columns=vertices)
    for v,u in self.arestas:
      self.matriz.loc[v,u] = 1
      if not self.dirigido:
        self.matriz.loc[u,v] = 1
    self.geraGrafo()

  def geraGrafo(self):
    if self.dirigido:
      G = nx.DiGraph()
    else:
      G = nx.Graph()
    G.add_edges_from(self.arestas)
    nx.draw(G, with_labels=True)
    plt.savefig("grafo.png")
    
  def isAdjacente(self, v, u):
    if u in self.matriz.index and v in self.matriz.index:
      aresta = self.matriz.loc[v,u]
      return "Sim" if aresta == 1 else "Não"
    else:
      return 'Vertices Incorretos'

  # verificar grau vendo o tipo
  def grauVertice(self, v):
    if v in self.matriz.index:
      if self.dirigido:
        return self.grauVerticeD(v)
      else:
        return self.grauVerticeND(v)
    else:
      return 'Vertice Incorreto'

  def grauVerticeD(self, v):
    emissao = sum(self.matriz.loc[v])
    recepcao = sum(self.matriz.loc[:,v])
    return {'Emissão': int(emissao),'Recepção': int(recepcao)}
    
  def grauVerticeND(self, v):
    return int(sum(self.matriz.loc[v]))

  def vizinhos(self, v):
    if v in self.matriz.index:
      linha = self.matriz.loc[v] == 1
      vertices = self.matriz.loc[linha].index
      return list(vertices)
    else:
      return 'Vertice Incorreto'

  def visitarArestas(self, v):
    if v in self.matriz.index:
      aux = defaultdict(list)
      visitados = defaultdict(list)
      for x in self.matriz.index:
        for y in self.matriz.columns:
          if self.matriz.loc[x][y] == 1:
            aux[x].append(y)
        visitados[x].append(False)
      fila = []
      fila.append(v)
      visitados[v] = True
      sequencia = ""
      while fila:
        v = fila.pop(0)
        for x in aux[v]:
          if visitados[x] == [False]: 
            fila.append(x)
            visitados[x] = True
        if fila:
          sequencia = sequencia + v + " --> "
        else :
          sequencia = sequencia + v 
      return sequencia
    else:
      return 'Vertice Incorreto'