# 定义图中节点的数据结构
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbour(self, nbr, weight=0):
        self.connectedTo[nbr] = Vertex(nbr)

    def __str__(self):
        return str(self.id) + 'connectedTo' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.values()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def __iter__(self):
        return iter(self.connectedTo.keys())


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, item):
        return item in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)

        self.vertList[f].addNeighbour(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    # def __iter__(self):
    #     return iter(self.vertList.values())


if __name__ == '__main__':
    # n = int(input())  # 节点数
    # m = int(input())  # 边数
    n, m = input().split(' ')
    n = int(n)
    m = int(m)
    g = Graph()
    for i in range(0, m):
        v1, v2 = input().split(' ')
        g.addEdge(v1, v2)
        g.addEdge(v2, v1)
    # for i in g.vertList.keys():
    #     list_1 = []
    #     list_2 = []
    #     list_1.append(g.vertList[i])
    #     x = 0
    #     while len(list_1) != 0 and x < 5:
    #         temp = list_1.pop(0)
    #         list_1 + list(temp.getConnections())
    #         n = n + 1
    #         list_2.append(temp)
    #     print(i + ':' + str(len(list_2) / n * 100) + '%')
    from pythonds.graphs import Graph


    class DFSGraph(Graph):
        def __init__(self):
            super().__init__()
            self.time = 0

        def dfs(self):
            for aVertex in self:
                aVertex.setColor('white')
                aVertex.setPred(-1)
            for aVertex in self:
                if aVertex.getColor() == 'white':
                    self.dfsvisit(aVertex)

        def dfsvisit(self, startVertex):
            startVertex.setColor('gray')
            self.time += 1
            startVertex.setDiscovery(self.time)
            for nextVertex in startVertex.getConnections():
                if nextVertex.getColor() == 'white':
                    nextVertex.setPred(startVertex)
                    self.dfsvisit(nextVertex)
            startVertex.setColor('black')
            self.time += 1
            startVertex.setFinish(self.time)
    for i in g.vertList.keys():

