
from collections import defaultdict
from typing import OrderedDict

class Graph():
	def __init__(self,vertices):
		self.graph = defaultdict(list)
		self.V = vertices

	def addEdge(self,u,v):
		self.graph[u].append(v)

	def isCyclicUtil(self, v, visited, recStack):

		# Mark current node as visited and
		# adds to recursion stack
		visited[v] = True
		recStack[v] = True

		# Recur for all neighbours
		# if any neighbour is visited and in
		# recStack then graph is cyclic
		for neighbour in self.graph[v]:
			if visited[neighbour] == False:
				if self.isCyclicUtil(neighbour, visited, recStack) == True:
					return True
			elif recStack[neighbour] == True:
				return True

		# The node needs to be poped from
		# recursion stack before function ends
		recStack[v] = False
		return False

	# Returns true if graph is cyclic else false
	def isCyclic(self):
		visited = [False] * (self.V + 1)
		recStack = [False] * (self.V + 1)
		for node in range(self.V):
			if visited[node] == False:
				if self.isCyclicUtil(node,visited,recStack) == True:
					return True
		return False


# from collections import OrderedDict
input_lines=[]
w=[]
edge_list=[]
dict={}
with open('input.txt') as f:
    input_lines=f.readlines()

c=0
for line in input_lines:
    print(line)
    if c==0:
        g = Graph(int(line))
    else :
        line=line.split(" ")
        print(line)
        temp=(int(line[0]),int(line[1]))
        # temp.append(int(line[0]))
        # temp.append(int(line[1]))
        dict[temp]= float(line[2])
        edge_list.append(temp)
        w.append(float(line[2]))
    c=c+1
print(dict)
dict1=sorted(dict.items(),key=lambda x:x[1])
# dict1 = OrderedDict(sorted(dict.items())) #inbuilt function for sorting based on the value in dict
print("sorted based on weight is "+str(dict1))
# count=0
# for line in input_lines:
#     print("Edge: "+str(edge_list[count]))
#     print("Weight of "+str(edge_list[count])+ "is "+str(w[count]))
#     count=count+1

#reversed dict
r_dict=OrderedDict(reversed())
print()
# #sort the edge lists
for 


# Python program to detect cycle
# in a graph





g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
if g.isCyclic() == 1:
	print("Graph has a cycle")
else:
	print("Graph has no cycle")

# Thanks to Divyanshu Mehta for contributing this code
