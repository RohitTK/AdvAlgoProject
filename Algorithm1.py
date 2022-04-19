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
from DisjointSet import DisjointSet

# Take an empty list
independentSet = {}

# Loading the graph from the file
inputGraph = Graph()
inputGraph.loadGraphFromFile(r"Input files\input.txt")
# inputGraph.loadGraphFromFile(r"Input files\input2.txt")

# Printing the graph and edge list
# inputGraph.printAdjMatrix()
print("The edge list: ")
inputGraph.printEdgeList()

edgeCount = 0

ds = DisjointSet(inputGraph.vertexList)

# Sorting the weights in non-increasing order
sorted_edges = dict(sorted(inputGraph.edgeList.items(), key=lambda x: x[1], reverse=True))

print(f"\nAfter sorting based on weights:\n{sorted_edges}")

for key, value in sorted_edges.items():
    vertexU = key[0]
    vertexV = key[1]
    weight = value

    mainParentU = ds.find(vertexU)
    mainParentV = ds.find(vertexV)

    if mainParentU != mainParentV:
        edgeCount += 1
        independentSet[(vertexU, vertexV)] = weight
        ds.union(mainParentU, mainParentV)

print("\nThe maximum weight independent set in a graphic matroid: ")
print(independentSet)
