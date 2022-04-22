# Reduction of general Steiner tree problem to metric Steiner tree

"""
Algorithm Steps:

Step 1: For the given graph input, a new complete graph needs to be created where
        the cost of edge (u,v) needs to be the shortest u-v path. (Metric Closure)
Step 2: To find the shortest path, we can use the Dijkstra algorithm.

Expected Input: Weighted Graph and Required Vertices
Expected Output: A complete weighted graph (Satisfying triangle inequality) and a set of required vertices
"""
import sys

from Graph import Graph


input_graph_path = r'Input files/weighted_graph_steiner.txt'
# input_graph_path = r'Input files/input2.txt'
required_vertices_path = r'Input files/required_vertices.txt'

file_data = open(required_vertices_path)

required_vertices = [int(i) for i in file_data.readlines()[0].split(" ")]

print("The required vertices are:", required_vertices)

input_graph = Graph()
input_graph.load_graph_from_file(input_graph_path)

print("The adjacency matrix for the input Graph")

input_graph.print_edge_list()
input_graph.print_adjacency_matrix()


def get_minimum_vertex(mst, key):
    min_key = sys.maxsize
    vertex = -1
    for i in range(input_graph.vertex_count):
        if not mst[i] and min_key > key[i]:
            min_key = key[i]
            vertex = i
    return vertex


def compute_shortest_path(src_vertex, in_graph, out_graph):
    shortest_path = [0 for _ in range(in_graph.vertex_count)]
    distance = [sys.maxsize for _ in range(in_graph.vertex_count)]

    distance[src_vertex] = 0

    for i in range(in_graph.vertex_count):
        vertex_u = get_minimum_vertex(shortest_path, distance)
        shortest_path[vertex_u] = 1

        for vertex_v in range(in_graph.vertex_count):
            if in_graph.adjacency_matrix[vertex_u][vertex_v] > 0:
                if in_graph.adjacency_matrix[vertex_u][vertex_v] != sys.maxsize and not shortest_path[vertex_v]:
                    sum = in_graph.adjacency_matrix[vertex_u][vertex_v] + distance[vertex_u]
                    if distance[vertex_v] > sum:
                        distance[vertex_v] = sum

    for i in range(in_graph.vertex_count):
        out_graph.add_edge(src_vertex, i, distance[i])


output_graph = Graph(vertex_count=input_graph.vertex_count)

# Compute the shortest path for each vertex
for source_vertex in input_graph.vertex_list:
    compute_shortest_path(src_vertex=source_vertex, in_graph=input_graph, out_graph=output_graph)

print("\nThe adjacency matrix for complete weighted graph is: ")
output_graph.print_adjacency_matrix()

print("\nThe edge list for complete weighted graph is: ")
output_graph.print_edge_list()

print("\nThe required vertices are:", required_vertices)
