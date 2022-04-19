# Reduction of general Steiner tree problem to metric Steiner tree

"""
Algorithm Steps:

Step 1: For the given graph input, a new complete graph needs to be created where
        the cost of edge (u,v) needs to be the shortest u-v path. (Metric Closure)
Step 2: To find the shortest path, we can use the Dijkstra algorithm.

Expected Input: Weighted Graph and Required Vertices
Expected Output: A complete weighted graph (Satisfying triangle inequality) and a set of required vertices
"""
from Graph import Graph

required_vertices_path = r'Input files/required_vertices.txt'
input_graph_path = r'Input files/input.txt'
# input_graph_path = r'Input files/input2.txt'

file_data = open(required_vertices_path)

required_vertices = [int(i) for i in file_data.readlines()[0].split(" ")]

print("The required vertices are:", required_vertices)

inputGraph = Graph()
inputGraph.loadGraphFromFile(input_graph_path)

print("The adjacency matrix for the input Graph")

inputGraph.printEdgeList()
inputGraph.printAdjacencyMatrix()


def getMinimumVertex(mst, key):
    minKey = 9999
    vertex = -1
    for i in range(inputGraph.vertexCount):
        if not mst[i] and minKey > key[i]:
            minKey = key[i]
            vertex = i
    return vertex


def dijkstra(srcVertex, outputGraph):
    spt = [0 for i in range(inputGraph.vertexCount)]
    distance = [9999 for i in range(inputGraph.vertexCount)]

    distance[srcVertex] = 0

    for i in range(inputGraph.vertexCount):
        vertexU = getMinimumVertex(spt, distance)
        spt[vertexU] = True

        for vertexV in range(inputGraph.vertexCount):
            if inputGraph.adjacencyMatrix[vertexU][vertexV] > 0:
                if not spt[vertexV] and inputGraph.adjacencyMatrix[vertexU][vertexV] != 9999:
                    sum = inputGraph.adjacencyMatrix[vertexU][vertexV] + distance[vertexU]
                    if sum < distance[vertexV]:
                        distance[vertexV] = sum

    for i in range(inputGraph.vertexCount):
        outputGraph.addEdge(srcVertex, i, distance[i])


outputGraph = Graph(vertexCount=inputGraph.vertexCount)

for srcVertex in inputGraph.vertexList:
    dijkstra(srcVertex, outputGraph)

print("\nThe adjacency matrix for complete weighted graph is: ")
outputGraph.printAdjacencyMatrix()

print("\nThe edge list for complete weighted graph is: ")
outputGraph.printEdgeList()

print("\nThe required vertices are:", required_vertices)
