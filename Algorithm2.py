# Reduction of general Steiner tree problem to metric Steiner tree

"""
Algorithm Steps:

Step 1: For the given graph input, a new complete graph needs to be created where
        the cost of edge (u,v) needs to be the shortest u-v path. (Metric Closure)
Step 2: To find the shortest path, we can use the Dijkstra algorithm.

Expected Input: Weighted Graph and Required Vertices
Expected Output: A complete weighted graph (Satisfying triangle inequality) and a set of required vertices
"""
from Graph import Graph

required_vertices_path = r'Input files/required_vertices.txt'
input_graph_path = r'Input files/input.txt'
# input_graph_path = r'Input files/input2.txt'

file_data = open(required_vertices_path)

required_vertices = [int(i) for i in file_data.readlines()[0].split(" ")]

print("The required vertices are:", required_vertices)

input_graph = Graph()
input_graph.load_graph_from_file(input_graph_path)

print("The adjacency matrix for the input Graph")

input_graph.print_edge_list()
input_graph.print_adjacency_matrix()


def get_minimum_vertex(mst, key):
    min_key = 9999
    vertex = -1
    for i in range(input_graph.vertex_count):
        if not mst[i] and min_key > key[i]:
            min_key = key[i]
            vertex = i
    return vertex


def dijkstra(src_vertex, output_graph):
    spt = [0 for _ in range(input_graph.vertex_count)]
    distance = [9999 for _ in range(input_graph.vertex_count)]

    distance[src_vertex] = 0

    for i in range(input_graph.vertex_count):
        vertex_u = get_minimum_vertex(spt, distance)
        spt[vertex_u] = True

        for vertex_v in range(input_graph.vertex_count):
            if input_graph.adjacency_matrix[vertex_u][vertex_v] > 0:
                if not spt[vertex_v] and input_graph.adjacency_matrix[vertex_u][vertex_v] != 9999:
                    sum = input_graph.adjacency_matrix[vertex_u][vertex_v] + distance[vertex_u]
                    if sum < distance[vertex_v]:
                        distance[vertex_v] = sum

    for i in range(input_graph.vertex_count):
        output_graph.add_edge(src_vertex, i, distance[i])


output_graph = Graph(vertex_count=input_graph.vertex_count)

for srcVertex in input_graph.vertex_list:
    dijkstra(srcVertex, output_graph)

print("\nThe adjacency matrix for complete weighted graph is: ")
output_graph.print_adjacency_matrix()

print("\nThe edge list for complete weighted graph is: ")
output_graph.print_edge_list()

print("\nThe required vertices are:", required_vertices)
