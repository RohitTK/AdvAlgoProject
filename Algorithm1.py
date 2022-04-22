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
independent_set = {}

# Loading the graph from the file
input_graph = Graph()
input_graph.load_graph_from_file(r"Input files\weighted_graph.txt")
# input_graph.load_graph_from_file(r"Input files\input2.txt")

# Printing the graph and edge list
# input_graph.print_adjacency_matrix()
print("The edge list: ")
input_graph.print_edge_list()

edge_count = 0

ds = DisjointSet(input_graph.vertex_list)

# Sorting the weights in non-increasing order
sorted_edges = dict(sorted(input_graph.edge_list.items(), key=lambda x: x[1], reverse=True))

print(f"\nAfter sorting based on weights:\n{sorted_edges}")

for key, value in sorted_edges.items():
    vertex_u = key[0]
    vertex_v = key[1]
    weight = value

    main_parent_u = ds.find(vertex_u)
    main_parent_v = ds.find(vertex_v)

    if main_parent_u != main_parent_v:
        edge_count += 1
        independent_set[(vertex_u, vertex_v)] = weight
        ds.union(main_parent_u, main_parent_v)

print("\nThe maximum weight independent set in a graphic matroid: ")
print(independent_set)
