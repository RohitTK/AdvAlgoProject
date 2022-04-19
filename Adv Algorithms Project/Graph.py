class Graph:
    def __init__(self):
        self.adjMatrix = None
        self.vertexCount = None
        self.edgeList = {}

    def loadGraphFromFile(self, path):
        file_data = open(path)
        self.vertexCount = int(file_data.readline())
        self.adjMatrix = [[0] * self.vertexCount for _ in range(self.vertexCount)]
        for line in file_data.readlines()[1:]:
            line = line.split(" ")
            self.addEdge(int(line[0]), int(line[1]), float(line[2]))

    def addEdge(self, vertex1, vertex2, weight):
        self.adjMatrix[vertex1][vertex2] = weight
        self.adjMatrix[vertex2][vertex1] = weight
        self.edgeList[(vertex1, vertex2)] = weight

    def printAdjMatrix(self):
        print('', end='\t')
        for i in range(self.vertexCount):
            print(f'{i}', end='\t\t')
        print('')
        for i in range(self.vertexCount):
            print(i, end='\t')
            for j in range(self.vertexCount):
                print(self.adjMatrix[i][j], end='\t\t')
            print('')

    def printEdgeList(self):
        print(str(self.edgeList))
