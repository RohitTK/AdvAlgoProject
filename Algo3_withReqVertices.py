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


required_vertices_path = r'Input files/required_vertices.txt'
input_graph_path = r'Input files/input2.txt'



#reading input data
graph_data = open(input_graph_path)
total_no_of_vertices = int(graph_data.readline())
edges_data = graph_data.readlines()[1:]
print("Total number of vertices in the graph:-" + str(total_no_of_vertices))


#reading required vertices data
file_data = open(required_vertices_path)
required_vertices = [int(i) for i in file_data.readlines()[0].split(" ")]
print("The required vertices are:", required_vertices)


#vertex list can be added accordingly(previous code) or by following:
vertex_list=[i for i in range(total_no_of_vertices)]
print("vertex list:- "+str(vertex_list))



#getting Steiner vertices by removing required vertices from all vertices
steiner_list=list(set(vertex_list)-set(required_vertices))
print("Steiner list:- "+str(steiner_list))



#getting combination of steiner vertices
combination_of_steiner_vertices=[]
com=[c for i in range(len(steiner_list)) for c in combinations(steiner_list,i+1)]
print("combination of steiner vertices are:-" +str(com))
#need to right trim to eliminate the , at the end


"""
Algorithm 3:
    1. Use dict={} to store the all possible MST's with all combination of steiner vertices as key and weight of tree as value
    2. return the MST among above dict which is least cost

Psuedocode for all MST's:
for i in steiner_list:
    temp=required_vertices.append(for j in i) #bcz i may contain(0) or (0,1) or (0,2)...
    minimumSpanningTree(temp) # call MST on these vertices
    
"""
