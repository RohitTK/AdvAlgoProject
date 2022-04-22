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
import sys
from itertools import combinations
from Graph import Graph

# Loading the graph from the file
input_graph = Graph()
# inputGraph.load_graph_from_file(r"Input files\input.txt")
input_graph.load_graph_from_file(r"Input files\weighted_graph.txt")

# Printing the graph and edge list
print("The edge list: ")
input_graph.print_edge_list()

mst_list = input_graph.get_minimum_spanning_tree()
print("\nMinimum Spanning Tree: ")
print(mst_list)

# for degree of each vertex
odd_degree_vertices = []

mst = Graph(input_graph.vertex_count)

for edge, weight in mst_list.items():
    mst.add_edge(vertex1=edge[0], vertex2=edge[1], weight=weight)

mst.print_adjacency_matrix()

for i in range(mst.vertex_count):
    count = 0  # for degree of each vertex
    for j in range(mst.vertex_count):
        if mst.adjacency_matrix[i][j] != 0:
            count += 1
    # Appending to the list if odd degree
    if (count % 2) != 0:
        odd_degree_vertices.append(i)

print("\nOdd degree vertices are:", odd_degree_vertices)
# print("Odd Vertices length is:"+str(len(odd_degree_vertex)))

# Initializing Euler graph with MST
euler = Graph(vertex_count=input_graph.vertex_count)

for ((vertex1, vertex2), weight) in mst_list.items():
    euler.add_edge(vertex1=vertex1, vertex2=vertex2, weight=weight)

# Computing minimum cost perfect matching
minimum_cost_perfect_matching = []
min_cost = sys.maxsize

# possible_pairs = []


if len(odd_degree_vertices) > 2:
    possible_combinations = list(combinations(list(combinations(odd_degree_vertices, 2)),
                                              int(len(odd_degree_vertices)/2)))

    for i in possible_combinations:
        temp = []
        for j in i:
            temp.extend(j)
        # No common vertex should be present in edges
        if len(set(temp)) == len(odd_degree_vertices):
            # possible_pairs.append(i)
            total_weight = sum([input_graph.adjacency_matrix[j[0]][j[1]] for j in i])
            if 0 < total_weight < min_cost:
                min_cost = sum([input_graph.adjacency_matrix[j[0]][j[1]] for j in i])
                minimum_cost_perfect_matching = list(i)
elif len(odd_degree_vertices) == 2:
    minimum_cost_perfect_matching = [tuple(odd_degree_vertices)]
    min_cost = input_graph.adjacency_matrix[odd_degree_vertices[0]][odd_degree_vertices[1]]
else:
    print("No pairs found")

print("\nMinimum Cost Perfect Matching:", minimum_cost_perfect_matching, "with cost =", min_cost)

# Merging minimum cost perfect matching into MST
for edge in minimum_cost_perfect_matching:
    euler.add_edge(vertex1=edge[0], vertex2=edge[1], weight=min_cost)


euler.print_adjacency_matrix()

visited_vertices = []
dfs_path = {}

print("\nEuler Tour: ")
euler.get_DFS(dfs_path=dfs_path, visited_vertices=visited_vertices)

print(dfs_path)
print(visited_vertices)

print("Total cost = ", sum(dfs_path.values()))
