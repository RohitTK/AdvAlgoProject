# The 2-approximation for the metric Traveling Salesman problem.

"""

Algorithm Steps:

Step 1: Find the MST of the Graph input
Step 2: Double every edge of the MST to obtain an Eulerian Graph
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

euler = Graph(inputGraph.vertexCount)

for edge, weight in MST.items():
    euler.addEdge(vertex1=edge[0], vertex2=edge[1], weight=weight)

visited_vertices = []
dfs_path = {}

print("\nEuler Tour: ")
euler.getDFS(dfs_path=dfs_path, visited_vertices=visited_vertices)

print(visited_vertices)
print(dfs_path)
print("Total cost = ", sum(dfs_path.values()))

