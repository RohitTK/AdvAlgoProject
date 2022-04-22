# Python program to detect cycle
# in a graph

from collections import defaultdict

class Graph():
	def __init__(self, vertices):
		self.graph = defaultdict(list)
		self.V = vertices

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def removeEdge(self, u, v):
		self.graph[u].remove(v)

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
		visited = [False] * self.V
		recStack = [False] * self.V
		for node in range(self.V):
			if visited[node] == False:
				if self.isCyclicUtil(node, visited, recStack) == True:
					return True
		return False

# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 2)
# g.add_edge(2, 0)
# g.add_edge(2, 3)
# if g.isCyclic() == 1:
# 	print ("Graph has a cycle")
# else:
# 	print ("Graph has no cycle")

# Thanks to Divyanshu Mehta for contributing this code=  Not JP


#our's code

def sorting_dict(dict_data): 
    return dict(sorted(dict_data.items(), key= lambda x:x[1], reverse= True))
#above method is taken as reference from https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.php 


try:
    file_data=open("input2.txt")
    no_of_vertices=int(file_data.readline())
    edges_data=file_data.readlines()[0:]
except:
    print("Please check the input file")

print("Total number of vertices in the graph:-" +str(no_of_vertices))


w=[]
edge_list=[]
dic={}

print(edges_data)
for line in edges_data:
    # print(line)
    line=line.split(" ")
    # print(line)
    temp=(int(line[0]),int(line[1]))
    # temp.append(int(line[0]))
    # temp.append(int(line[1]))
    dic[temp]= float(line[2])
    edge_list.append(temp)
    w.append(float(line[2]))

print("Input in dictionary format is:- "+str(dic))
# print(dic)
sorted_dict=sorting_dict(dic)
print("After sorting :-"+str(sorted_dict))


g = Graph(no_of_vertices)
answer={}

for key,value in sorted_dict.items():
    i=key[0]
    j=key[1]
    g.addEdge(i,j)
    if g.isCyclic()==1:
        g.removeEdge(i,j)
    else:
        answer[key]=value


print("final answer is")
print(answer)
