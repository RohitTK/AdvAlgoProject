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

required_vertices_path = r'../Input files/required_vertices.txt'
input_graph_path = r'../Input files/input2.txt'

# reading input data
graph_data = open(input_graph_path)
total_no_of_vertices = int(graph_data.readline())
edges_data = graph_data.readlines()[1:]
print("Total number of vertices in the graph:-" + str(total_no_of_vertices))

# reading required vertices data
file_data = open(required_vertices_path)
required_vertices = [int(i) for i in file_data.readlines()[0].split(" ")]
print("The required vertices are:", required_vertices)

# vertex list can be added accordingly(previous code) or by following:
vertex_list = [i for i in range(total_no_of_vertices)]
print("vertex list:- " + str(vertex_list))

# getting Steiner vertices by removing required vertices from all vertices
steiner_list = list(set(vertex_list) - set(required_vertices))
print("Steiner list:- " + str(steiner_list))

# getting combination of steiner vertices
combination_of_steiner_vertices = []
com = [list(c) for i in range(len(steiner_list)) for c in combinations(steiner_list, i + 1)]
print("combination of steiner vertices are:-" + str(com))
# need to right trim to eliminate the , at the end

inputGraph = Graph()
inputGraph.load_graph_from_file(r"Input files\input2.txt")


least_spanning_tree = inputGraph.get_minimum_spanning_tree(required_vertices)
least_cost = sum(least_spanning_tree.values())
vertices_used = required_vertices

print("Spanning tree for the vertices ", required_vertices, "is:")
print(least_spanning_tree)
print("Total cost = ", least_cost, "\n")

for steiner_vertices in com:
    total_vertices = required_vertices + steiner_vertices
    print("Spanning tree for the vertices ", total_vertices, "is:")
    spanning_tree = inputGraph.get_minimum_spanning_tree(total_vertices)
    print(spanning_tree)
    total_cost = sum(spanning_tree.values())
    print("Total cost = ", total_cost, "\n")
    if least_cost > total_cost:
        least_cost = total_cost
        vertices_used = total_vertices
        least_spanning_tree = spanning_tree

print("Vertices used for the Steiner Tree: ", vertices_used,
      "\nSteiner vertices used:", list(set(vertices_used) - set(required_vertices)))

print("The Steiner tree:")
print(least_spanning_tree)

print("Total Cost = ", least_cost)

"""
Algorithm 3:
    1. Use dict={} to store the all possible MST's with all combination of steiner vertices as key and weight of tree as value
    2. return the MST among above dict which is least cost

Psuedocode for all MST's:
for i in steiner_list:
    temp=required_vertices.append(for j in i) #bcz i may contain(0) or (0,1) or (0,2)...
    minimumSpanningTree(temp) # call MST on these vertices
    
"""
