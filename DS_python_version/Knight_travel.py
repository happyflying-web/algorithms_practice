def getlegalMoves(x, y, bdSize):
    newMoves = []
    # 马只能走日字格
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                   (1. - 2), (1, 2), (2, -1), (2, 1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):
            newMoves.append((newX, newY))
    return newMoves


def legalCoord(x, bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return False


def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeID = posToNodeId(row, col, bdSize)
            newPositions = getlegalMoves(row, col, bdSize)
            for e in newPositions:
                nid = posToNode(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeID, nid)
    return ktGraph


def posToNodeId(row, col, bdSize):
    return row * bdSize + col
