# The 2-approximation for metric Steiner tree

"""
Algorithm Steps:

Step 1: For the given complete weighted graph input and set of required vertices,
        a MST needs to be found on the set of required vertices.
Step 2: MST Logic

Expected Input: A complete weighted graph (Satisfying triangle inequality) and a set of required vertices
Expected Output: Edge list of a Steiner Tree
"""

from Graph import Graph

# Loading the graph from the file
inputGraph = Graph()
# inputGraph.loadGraphFromFile(r"Input files\input.txt")
inputGraph.loadGraphFromFile(r"Input files\input2.txt")

# Printing the graph and edge list
# inputGraph.printAdjMatrix()
print("The edge list: ")
inputGraph.printEdgeList()

# print("\nMinimum Spanning Tree: ")
print(inputGraph.getMinimumSpanningTree())
