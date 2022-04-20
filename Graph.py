from DisjointSet import DisjointSet


class Graph:
    def __init__(self, vertexCount=0):
        self.vertexCount = vertexCount
        self.adjacencyMatrix = [[0] * self.vertexCount for _ in range(self.vertexCount)] if vertexCount > 0 else None
        self.edgeList = {}
        self.vertexList = []

    def loadGraphFromFile(self, path):
        file_data = open(path)
        self.vertexCount = int(file_data.readline())
        self.adjacencyMatrix = [[0] * self.vertexCount for _ in range(self.vertexCount)]
        for line in file_data.readlines()[1:]:
            line = line.split(" ")
            self.addEdge(int(line[0]), int(line[1]), float(line[2]))
            if int(line[0]) not in self.vertexList:
                self.vertexList.append(int(line[0]))
            if int(line[1]) not in self.vertexList:
                self.vertexList.append(int(line[1]))

    def addEdge(self, vertex1, vertex2, weight):
        self.adjacencyMatrix[vertex1][vertex2] = weight
        self.adjacencyMatrix[vertex2][vertex1] = weight
        self.edgeList[(vertex1, vertex2)] = weight

    def printAdjacencyMatrix(self):
        print('', end='\t')
        for i in range(self.vertexCount):
            print(f'{i}'.rjust(10), end=' ')
        print('')
        for i in range(self.vertexCount):
            print(i, end='\t')
            for j in range(self.vertexCount):
                print(str(self.adjacencyMatrix[i][j]).rjust(10), end=' ')
            print('')

    def printEdgeList(self):
        print(str(self.edgeList))

    def getMinimumSpanningTree(self, customVertices=None):
        edgeCount = 0
        minimumSpanningTree = {}

        ds = DisjointSet(customVertices) if customVertices else DisjointSet(self.vertexList)

        # Sorting the weights in non-increasing order
        sorted_edges = dict(sorted(self.edgeList.items(), key=lambda x: x[1]))

        if customVertices:
            for key, value in self.edgeList.items():
                if key[0] not in customVertices or key[1] not in customVertices:
                    sorted_edges.pop(key)

        for key, value in sorted_edges.items():
            vertexU = key[0]
            vertexV = key[1]
            weight = value

            mainParentU = ds.find(vertexU)
            mainParentV = ds.find(vertexV)

            if mainParentU != mainParentV:
                edgeCount += 1
                minimumSpanningTree[(vertexU, vertexV)] = weight
                ds.union(mainParentU, mainParentV)

        return minimumSpanningTree

    def getDFS(self, start=0, dfs_path=None, visited_vertices=None):
        if visited_vertices is None:
            visited_vertices = []
        if dfs_path is None:
            dfs_path = {}

        visited_vertices.append(start)

        for i in range(self.vertexCount):
            if self.adjacencyMatrix[start][i] != 0 and i not in visited_vertices:
                dfs_path[(start, i)] = self.adjacencyMatrix[start][i]
                self.getDFS(i, dfs_path, visited_vertices)
