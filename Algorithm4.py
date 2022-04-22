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
input_graph = Graph()
input_graph.load_graph_from_file(r"Input files\weighted_graph.txt")
# inputGraph.load_graph_from_file(r"Input files\input2.txt")

# Printing the graph and edge list
# inputGraph.printAdjMatrix()
print("The edge list: ")
input_graph.print_edge_list()


mst = input_graph.get_minimum_spanning_tree()
print("\nMinimum Spanning Tree: ")
print(mst)

euler = Graph(input_graph.vertex_count)

for edge, weight in mst.items():
    euler.add_edge(vertex1=edge[0], vertex2=edge[1], weight=weight)

visited_vertices = []
dfs_path = {}

print("\nEuler Tour: ")
euler.get_DFS(dfs_path=dfs_path, visited_vertices=visited_vertices)

print(visited_vertices)
print(dfs_path)
print("Total cost = ", sum(dfs_path.values()))

