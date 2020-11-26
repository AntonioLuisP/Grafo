from Grafo import Grafo
import PySimpleGUI as sg
import os


class Interface:

  def escolheArquivo(self):
    layout = [
      [sg.Text('Escolha o arquivo .txt onde está descrito o grafo')],
      [sg.FileBrowse(key='caminho')],
      [sg.Button('Continuar'),sg.Button('Sair')],
    ]
    janela = sg.Window("Análise de grafo").layout(layout)
    button, values = janela.Read(close=True)
    if button == 'Continuar':
      if values['caminho']:
        try:
          info = self.infoArquivo(values['caminho'])
          print()
          tipo = info['tipo']
          arestas = info['arestas']
          vertices = info['vertices']
          self.grafo = Grafo(tipo, arestas, vertices)
          janela.close()
          self.matriz()
        except:
          self.escolheArquivo()
      else:
        self.escolheArquivo()
    if button == 'Sair':
      janela.close()
    if button == sg.WIN_CLOSED:
      janela.close()

  def matriz(self):
    grafo = [ 
      [sg.Text("Grafo")],
      [sg.Image(filename=os.getcwd()+'\grafo.png',key="imagem")],    
    ] 
    perguntas = [      
      [sg.Text("Matriz de Adjacência")],
      [sg.Text("Grafo"+"Dirigido" if self.grafo.dirigido else "Não Dirigido")],
      [sg.Text(self.grafo.matriz)],
      [sg.Button('Continuar')],
    ]
    layout = [
      [
        sg.Column(grafo),
        sg.VSeperator(),
        sg.Column(perguntas)
      ]
    ]

    janela = sg.Window("Análise de grafo").layout(layout)
    button, values = janela.Read(close=True)
    
    if button == 'Continuar':
      janela.close()
      self.principal()
    if button == sg.WIN_CLOSED:
      janela.close()

  def principal(self):
    perguntas = [
      [sg.Text('Verificar adjacencias entre vertices')],
      [sg.Text('Primeiro'), sg.Input(size=(25,0),key='adj_primeiro'), sg.Text('Segundo'), sg.Input(size=(25,0),key='adj_segundo')],
      [sg.Button('Verificar Adjacencia'),sg.Text('Resposta',size=(25,0), key='r_adjacencia')],
      [sg.Text('Verificar Grau do vertice')],
      [sg.Text('Digite um vértice'), sg.Input(size=(25,0),key='grau_vertice')],
      [sg.Button('Verificar Grau'),sg.Text('Resposta',size=(25,0),key='r_grau')],
      [sg.Text('Verificar Vizinho do vertice')],
      [sg.Text('Digite um vértice'), sg.Input(size=(25,0),key='vizinho_vertice')],
      [sg.Button('Verificar Vizinho'),sg.Text('Resposta',size=(25,0),key='r_vizinho')],
      [sg.Text('Visitar vertices do grafo')],
      [sg.Text('Digite um vértice'), sg.Input(size=(25,0),key='visita_vertice')],
      [sg.Button('Verificar visita'),sg.Text('Resposta',size=(25,0),key='r_visita')],
    ]
    grafo = [ 
      [sg.Text("Grafo")],
      [sg.Image(filename=os.getcwd()+'\grafo.png',key="-IMAGE-",)],    
    ]
    layout = [
      [
        sg.Column(grafo),
        sg.VSeperator(),
        sg.Column(perguntas),
      ]
    ]
    
    janela = sg.Window("Análise de grafo").layout(layout)
    status = True
    while status:
      button, values = janela.Read()
      if button == 'Verificar Adjacencia':
        r_adjacencia = self.grafo.isAdjacente(values['adj_primeiro'],values['adj_segundo'])
        janela['r_adjacencia'].Update(r_adjacencia)
      if button == 'Verificar Grau':
        r_grau = self.grafo.grauVertice(values['grau_vertice'])
        janela['r_grau'].Update(r_grau)    
      if button == 'Verificar Vizinho':
        r_vizinho = self.grafo.vizinhos(values['vizinho_vertice'])
        janela['r_vizinho'].Update(r_vizinho)    
      if button == 'Verificar visita':
        r_visita = self.grafo.visitarArestas(values['visita_vertice'])
        janela['r_visita'].Update(r_visita)    
      if button == sg.WIN_CLOSED:
        status = False
        janela.close()

    if button == sg.WIN_CLOSED:
      janela.close()

  def infoArquivo(self, caminho):
    arquivo = open(caminho, 'r')
    info = {}
    tipo = arquivo.readline().rstrip('\n')
    if tipo == 'D':
      tipo = True
    else:
      tipo = False
    arestas = []
    vertices = []
    for i in arquivo:
      linha = i.split(',')
      linha[0] = str(linha[0].rstrip('\n'))
      linha[1] = str(linha[1].rstrip('\n'))
      arestas.append((linha[0], linha[1]))
      if linha[0] not in vertices:
        vertices.append(linha[0])
      if linha[1] not in vertices:
        vertices.append(linha[1])
    info = {
      'tipo': tipo,
      'arestas': arestas,
      'vertices': vertices,
    }
    arquivo.close() 
    return info

tela = Interface()
tela.escolheArquivo()



