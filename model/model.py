import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}

    def buildGraph(self, minimo):
        self._grafo.clear()
        allNodes = DAO.getAeroportiMinCompagnie(minimo)
        allAirports = DAO.getAllAirports()
        for n in allAirports:
            self._idMap[n.ID] = n
        self._grafo.add_nodes_from(allNodes)
        self.addEdges()
        return True

    def addEdges(self):
        allConnessioni = DAO.getAllConnessioni(self._idMap)
        for c in allConnessioni:
            if c.A1 in self._grafo.nodes and c.A2 in self._grafo.nodes:
                self._grafo.add_edge(c.A1, c.A2, weight=c.Peso)

    def getVicini(self, origine):
        vicini = self._grafo.neighbors(origine)
        viciniTuple = []
        for v in vicini:
            viciniTuple.append((v, self._grafo[origine][v]["weight"]))
        viciniTuple.sort(key=lambda x: x[1], reverse=True)
        return viciniTuple

    def getNodes(self):
        return self._grafo.nodes

    def printGraphDetails(self):
        return f"Il grafo ha {len(self._grafo.nodes)} nodi e {len(self._grafo.edges)} archi"
