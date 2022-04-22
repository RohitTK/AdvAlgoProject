Team Members:
-> Jaya Prakash Reddy Veldanda (JV21K)
-> Kali Rohit Tanneeru (KT21N)
-> Mohan Krishna Medisetti (MM21CZ)
-> Shubhanka Reddy Chintakuntla (SC20IH)
-> Uday Kumar Kasha (UK21A)

========================================================================================================================
Input files present in the folder "Input files": weighted_graph.txt and required_vertices.txt
========================================================================================================================
Note:
-> The output edge list is displayed in the format {(u1, v1): w1, (u2, v2): w2, (u3, v3): w3 ..... (un, vn): wn}
   where u, v are the vertices, n is the number of vertices in the graph.
-> w is a float value that lies between 0 and 1.
========================================================================================================================

Steps to run:
To run the first algorithm:
-> Update the "weighted_graph.txt" where the first line is the number of vertices and every line after
   is a weighted edge in the format of u v w. This graph can be a simple weighted graph.
-> Run Algorithm1.py in the terminal using "python3 Algorithm1.py"
-> The returned output is the edge list of the maximum weight independent subset.

To run the second algorithm:
-> Update the "weighted_graph.txt" where the first line is the number of vertices and every line after
   is a weighted edge in the format of u v w. This graph can be a simple weighted graph.
-> Update the "required_vertices.txt" which needs to contain the set of required vertices separated by space.
-> Run Algorithm2.py in the terminal using "python3 Algorithm2.py"
-> The returned output is the edge list of the complete weighted graph which satisfies triangle inequality
   and the list of required vertices.

To run the third algorithm:
-> Update the "weighted_graph.txt" where the first line is the number of vertices and every line after is a weighted
   edge in the format of u v w. This needs a complete weighted graph as input that satisfies triangle inequality.
-> Update the "required_vertices.txt" which needs to contain the set of required vertices separated by space
-> Run Algorithm3.py in the terminal using "python3 Algorithm3.py"
-> The returned output is the edge list of the minimum spanning tree on the required vertices.

To run the fourth algorithm:
-> Update the "weighted_graph.txt" where the first line is the number of vertices and every line after is a weighted edge
   in the format of u v w. This needs a complete weighted graph as input.
-> Update the "required_vertices.txt" which needs to contain the set of required vertices separated by space
-> Run Algorithm4.py in the terminal using "python3 Algorithm4.py"
-> The returned output is the euler tour of the visited vertices and the total cost for the traversed path.

To run the fifth algorithm:
-> Update the "weighted_graph.txt" where the first line is the number of vertices and every line after is a weighted edge
   in the format of u v w. This needs a complete weighted graph as input.
-> Update the "required_vertices.txt" which needs to contain the set of required vertices separated by space.
-> Run Algorithm5.py in the terminal using "python3 Algorithm5.py"
-> The returned output is the euler tour of the visited vertices and the total cost for the traversed path.

========================================================================================================================
Contribution:

Algorithm 1: Greedy algorithm to find maximum-weight-independent set in a graphic matroid - Kali Rohit Tanneeru (KT21N)
Algorithm 2: Reduction of general Steiner tree problem to metric Steiner tree - Jaya Prakash Reddy Veldanda (JV21K)
Algorithm 3: The 2-approximation for metric Steiner tree - Mohan Krishna Medisetti (MM21CZ)
Algorithm 4: The 2-approximation for the metric Traveling Salesman problem - Shubhanka Reddy Chintakuntla (SC20IH)
Algorithm 5: The 3/2-approximation (Christofides) for the metric Traveling Salesman problem - Uday Kumar Kasha (UK21A)

========================================================================================================================