# Greedy algorithm to find maximum-weight-independent set in a graphic matroid

"""
Algorithm Steps:

Step 1: Take an empty list A
Step 2: Need to sort the edges in decreasing order by weights.
Step 3: Iterate through each element of the sorted array
Step 4: Check if A is still an independent set (acyclic) even after the element is added.
        If it is still independent, append the edge to the list A
Step 5: Return the list A

Expected Input: Weighted Graph
Expected Output: An independent acyclic set of edges of a graphic matroid.
"""
from Graph import Graph

# Take an empty list
independentSet = {}

# Loading the graph from the file
inputGraph = Graph()
inputGraph.loadGraphFromFile(r"Input files\input2.txt")

# Printing the graph and edge list
inputGraph.printAdjMatrix()
inputGraph.printEdgeList()

# Sorting the weights in non-increasing order
sorted_edges = dict(sorted(inputGraph.edgeList.items(), key=lambda x: x[1], reverse=True))

print(f"After sorting:\n{sorted_edges}")

for edge, weight in sorted_edges.items():
    independentSet[edge] = weight

print(independentSet)