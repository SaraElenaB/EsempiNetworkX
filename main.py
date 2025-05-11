import math
from dataclasses import dataclass

import networkx as nx

@dataclass
class Voto:
    punti: int
    nome: str

    def __eq__(self, other):
        return self.nome == other.nome

    def __hash__(self):
        return hash((self.punti, self.nome))
    #------------------------------------------------------------------------------------------------------------------------------

grafo_semplice = nx.Graph() #grafo semplice
grafo_diretto = nx.DiGraph() #grafo diretto

grafo_diretto.add_node(1)
grafo_diretto.add_node("Due")
grafo_diretto.add_node( Voto(24, "TdP"))
grafo_diretto.add_node(math.cos)

grafo_diretto.add_edge("Due", 1, attributoWeight=0.9) #non essendo diretto, avere da 1 a due o due a 1 cambia nulla

print(grafo_semplice.nodes) #puo sztampare grafi non omogenei
print(grafo_semplice.edges)

nBunch = [1,2,3,4,5,6,7,8,9]
grafo_diretto.add_nodes_from(nBunch)
print(f"Mostra i nodi: {grafo_diretto.nodes}")

eBunch = [ (4,6), (8,1), (2,9)]
#avessi messo un numero che non c'è tra i nodi, lo aggiunge
#se ti trovi con grafi che hanno il doppio dei nodi allora stai aggiungendo archi tramite l'id dei nodi e non con i nodi stessi
grafo_diretto.add_edges_from(eBunch)
print(f"Mostra gli archi: {grafo_diretto.edges}")

print(f"Mostra l'attributo {grafo_diretto.get_edge_data("Due", 1)}")
print(f"Accesso al nodo 4: {grafo_diretto[4]} ") #accedo al dict grafo dove ho associato al nodo 4 l'arco 6, 6 a sua volta la chiave di un dict che ha un dizionario con gli attributi (vuoto)
print(f"Accesso al nodo Due: {grafo_diretto["Due"]}") #associato a "Due" ho un nodo di arrivo:1 a cui c'è associato il dict con un attributo (oppure tutti gli attributi di quell'arco)
print(f"Accesso solo al dict degli attributi: {grafo_diretto["Due"][1]}")

#------------------------------------------------------------------------------------------------------------------------------