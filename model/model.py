import networkx as nx
from database.dao import DAO


class Model:
    def __init__(self):
        self.G = nx.Graph()

        self.rifugi_map = {}
        self.load_rifugi()
        self.connessioni = []

    def build_graph(self, year: int):
        """
        Costruisce il grafo (self.G) dei rifugi considerando solo le connessioni
        con campo `anno` <= year passato come argomento.
        Quindi il grafo avrà solo i nodi che appartengono almeno ad una c, non tutti quelli disponibili.
        :param year: anno limite fino al quale selezionare le connessioni da includere.
        """
        self.load_connessioni(year)
        for c in self.connessioni:
            ogg_rifugio1 = self.rifugi_map[c.id_rifugio1]
            ogg_rifugio2 = self.rifugi_map[c.id_rifugio2]
            self.G.add_edge(ogg_rifugio1, ogg_rifugio2,
                            distanza=c.distanza, difficolta=c.difficolta,
                            durata=c.durata, anno=c.anno)
        print('Grafo creato: ',self.G)
        return

        # TODO

    def get_nodes(self):
        """
        Restituisce la lista dei rifugi presenti nel grafo.
        :return: lista dei rifugi presenti nel grafo.
        """
        nodi = self.G.nodes()
        print('Nodi del grafo relativo: ',[nodo.id for nodo in nodi])
        return nodi
        # TODO

    def get_num_neighbors(self, node):
        """
        Restituisce il grado (numero di vicini diretti) del nodo rifugio.
        :param node: un rifugio (cioè un nodo del grafo)
        :return: numero di vicini diretti del nodo indicato
        """
        vicini = nx.neighbors(self.G, node)
        lista_vicini = list(vicini)
        print(f'Vicini di {node}: ', lista_vicini)
        grado = len(lista_vicini)
        print(f'Grado di {node}: ',grado)
        print()
        return grado
        # TODO

    def get_num_connected_components(self):
        """
        Restituisce il numero di componenti connesse del grafo.
        :return: numero di componenti connesse
        """
        n_componenti_connesse = nx.number_connected_components(self.G)
        print('Numero di componenti connesse: ',n_componenti_connesse)
        return n_componenti_connesse
        # TODO

    def get_reachable(self, start):
        """
        Deve eseguire almeno 2 delle 3 tecniche indicate nella traccia:
        * Metodi NetworkX: `dfs_tree()`, `bfs_tree()`
        * Algoritmo ricorsivo DFS
        * Algoritmo iterativo
        per ottenere l'elenco di rifugi raggiungibili da `start` e deve restituire uno degli elenchi calcolati.
        :param start: nodo di partenza, da non considerare nell'elenco da restituire.

        ESEMPIO
        a = self.get_reachable_bfs_tree(start)
        b = self.get_reachable_iterative(start)
        b = self.get_reachable_recursive(start)

        return a
        """
        ramoA = self.get_reachable_bfs_tree(start)
        ramoB = self.get_reachable_recursive(start)
        return ramoB
        # TODO
    def get_reachable_bfs_tree(self, start):
        rami = nx.bfs_tree(self.G, start)
        print(f'Nodi visitati a partire da {start}: ', rami.nodes )
        return rami

    def get_reachable_recursive(self, start):
        visitati = set()
        self.ricorsione(self.G, start, visitati)
        return list(visitati)

    def ricorsione(self, grafo, nodo, visitati):
        if nodo in visitati:
            return

        visitati.add(nodo)

        for vicino in grafo.neighbors(nodo):
            self.ricorsione(grafo, vicino, visitati)

    def load_rifugi(self):
        self.rifugi_map = DAO.get_all_rifugi()
        # print(self.rifugi_map)
        return

    def load_connessioni(self, year: int):
        self.connessioni = DAO.get_connessioni(year)
        return
