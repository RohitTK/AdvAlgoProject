# The 3/2-approximation (Christofides) for the metric Traveling Salesman problem.

"""

Algorithm Steps:

Step 1: Find the MST of the Graph input
Step 2: Compute a minimum cost perfect matching on the set of odd degree vertices.
        And then, need to add this matching to the MST to obtain an Eulerian Graph
Step 3: Find an Eulerian tour on this Eulerian Graph
Step 4: Need to output the visited vertices in the order of appearance in the Eulerian Tour

Expected Input: A weighted complete graph
Expected Output: A cycle of vertices/edges corresponding to the Travelling Salesman Problem.

"""

from Graph import Graph

# Loading the graph from the file
inputGraph = Graph()
inputGraph.loadGraphFromFile(r"Input files\input.txt")
# inputGraph.loadGraphFromFile(r"Input files\input2.txt")

# Printing the graph and edge list
# inputGraph.printAdjMatrix()
print("The edge list: ")
inputGraph.printEdgeList()

MST = inputGraph.getMinimumSpanningTree()
print("\nMinimum Spanning Tree: ")
print(MST)

# for degree of each vertex
odd_degree_vertex = []
print(inputGraph.adjacencyMatrix)
for i in range(inputGraph.vertexCount):
    count = 0  # for degree of each vertex
    for j in range(inputGraph.vertexCount):
        if inputGraph.adjacencyMatrix[i][j] != 0:
            count += 1
    if (count % 2) != 0:
        odd_degree_vertex.append(i)

print(odd_degree_vertex)
# print("Odd Vertices length is:"+str(len(odd_degree_vertex)))

# euler graph
euler = MST

# Putting new
for i in range(int(len(odd_degree_vertex) / 2)):
    a = int(odd_degree_vertex[i])
    b = int(odd_degree_vertex[i + 1])
    if inputGraph.edgeList[(a, b)] != None:
        euler[(a, b)] = inputGraph.edgeList[(a, b)]
    else:
        pass
        # Rohit, call Djikstra for cost from a to b
print(euler)
