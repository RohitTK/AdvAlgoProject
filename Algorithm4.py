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
inputGraph = Graph()
inputGraph.loadGraphFromFile(r"Input files\input.txt")
# inputGraph.loadGraphFromFile(r"Input files\input2.txt")

# Printing the graph and edge list
# inputGraph.printAdjMatrix()
print("The edge list: ")
inputGraph.printEdgeList()


MST=inputGraph.getMinimumSpanningTree()
print("\nMinimum Spanning Tree: ")
print(MST)


#Using DFS to get the path in MST
#calculate the total weight of MST