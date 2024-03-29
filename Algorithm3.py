# The 2-approximation for metric Steiner tree

"""
Algorithm Steps:

Step 1: For the given complete weighted graph input and set of required vertices,
        a MST needs to be found on the set of required vertices.
Step 2: MST Logic

Expected Input: A complete weighted graph (Satisfying triangle inequality) and a set of required vertices
Expected Output: Edge list of a Steiner Tree
"""

from itertools import combinations

from Graph import Graph

required_vertices_path = r'Input files/required_vertices.txt'
input_graph_path = r'Input files/weighted_graph.txt'

input_graph = Graph()
input_graph.load_graph_from_file(input_graph_path)

# print("Total number of vertices in the graph:-", input_graph.vertex_count)

print("Vertex list: ", input_graph.vertex_list)

# reading required vertices data
file_data = open(required_vertices_path)
required_vertices = [int(i) for i in file_data.readlines()[0].split(" ")]
print("The required vertices are:", required_vertices)

# getting Steiner vertices by removing required vertices from all vertices
# steiner_list = list(set(input_graph.vertex_list) - set(required_vertices))
# print("Steiner list:- " + str(steiner_list))

# getting combination of steiner vertices
# combination_of_steiner_vertices = [list(c) for i in range(len(steiner_list))
#                                    for c in combinations(steiner_list, i + 1)]
# print("combination of steiner vertices are:-" + str(combination_of_steiner_vertices))

# Initialization
least_spanning_tree = input_graph.get_minimum_spanning_tree(required_vertices)
least_cost = sum(least_spanning_tree.values())
vertices_used = required_vertices

print("\nThe Minimum Spanning tree on the required vertices is:")
print(least_spanning_tree)
print("\nTotal cost =", least_cost, "\n")

# for steiner_vertices in combination_of_steiner_vertices:
#     total_vertices = required_vertices + steiner_vertices
#     print("Spanning tree for the vertices", total_vertices, "is:")
#     spanning_tree = input_graph.get_minimum_spanning_tree(total_vertices)
#     print(spanning_tree)
#     total_cost = sum(spanning_tree.values())
#     print("Total cost =", total_cost, "\n")
#     if least_cost > total_cost:
#         least_cost = total_cost
#         vertices_used = total_vertices
#         least_spanning_tree = spanning_tree
#
# print("Vertices used for the Steiner Tree:", vertices_used,
#       "\nSteiner vertices used:", list(set(vertices_used) - set(required_vertices)))
#
# print("The Steiner tree:")
# print(least_spanning_tree)
#
# print("Total Cost =", least_cost)
