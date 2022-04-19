file_data = open("input.txt")
no_of_vertices = int(file_data.readline())
edges_data = file_data.readlines()[1:]

print("Total number of evrtices in the graph:-" + str(no_of_vertices))

G = [[0] * no_of_vertices for i in range(no_of_vertices)]

# print(edges_data)
for line in edges_data:
    # print(line)
    line = line.split(" ")
    G[int(line[0])][int(line[1])] = float(line[2])

# below code snippet is just for checking the input
for i in range(no_of_vertices):
    for j in range(no_of_vertices):
        print(G[i][j], end="\t\t")
    print("")
