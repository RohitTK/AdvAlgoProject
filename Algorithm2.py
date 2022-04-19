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

file_data = open(required_vertices_path)

required_vertices = [int(i) for i in file_data.readlines()[0].split(" ")]

print("The required vertices are:", required_vertices)

inputGraph = Graph()
inputGraph.loadGraphFromFile(input_graph_path)

inputGraph.printEdgeList()
inputGraph.printAdjacencyMatrix()


def getMinimumPathCost(srcVertex, destVertex, inputGraph):

    return -1


outputGraph = Graph(vertexCount=inputGraph.vertexCount)

for srcVertex in inputGraph.vertexList:
    for destVertex in inputGraph.vertexList:
        if srcVertex != destVertex:
            minCost = getMinimumPathCost(srcVertex, destVertex, inputGraph)
            outputGraph.addEdge(srcVertex, destVertex, minCost)

print("\nThe adjacency matrix for complete weighted graph is: ")
outputGraph.printAdjacencyMatrix()

print("\nThe edge list for complete weighted graph is: ")
outputGraph.printEdgeList()

print("\nThe required vertices are:", required_vertices)
