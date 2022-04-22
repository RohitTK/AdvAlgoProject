from Graph import Graph

# Loading the graph from the file
inputGraph = Graph()
# inputGraph.load_graph_from_file(r"Input files\input.txt")
inputGraph.load_graph_from_file(r"Input files\input2.txt")

# Printing the graph and edge list
# inputGraph.printAdjMatrix()
print("The edge list: ")
inputGraph.print_edge_list()


visited_vertices = []
dfs_path = {}

print("\nDFS: ")
inputGraph.get_DFS(dfs_path=dfs_path, visited_vertices=visited_vertices)

print(dfs_path)
print(visited_vertices)

print("\nMinimum Spanning Tree: ")
print(inputGraph.get_minimum_spanning_tree())

required_vertices = [0, 1, 2, 4]
print("\nMinimum Spanning Tree using required vertices", required_vertices, ":")
print(inputGraph.get_minimum_spanning_tree(required_vertices))

