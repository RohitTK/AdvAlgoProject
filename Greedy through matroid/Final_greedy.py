# Take input

# split accordingly

# use dict to store edge as key and weight as value

# sort the dictionary based on weight

# use a temp list to check the added edge to the graph cause a cyclic graph

# compare the edges in list, if not add the non exising edges to the temp and also to the graph

# if both edges are in temp list, it causes cyclic graph. So, shd not be added

# return the list of edges with weight


def sorting_dict(dict_data):
    return dict(sorted(dict_data.items(), key=lambda x: x[1], reverse=True))


# above method is taken as reference from https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.php


input_lines = []
w = []
edge_list = []
dic = {}
with open('input.txt') as f:
    input_lines = f.readlines()

for line in input_lines:
    # print(line)
    line = line.split(" ")
    # print(line)
    temp = (int(line[0]), int(line[1]))
    # temp.append(int(line[0]))
    # temp.append(int(line[1]))
    dic[temp] = float(line[2])
    edge_list.append(temp)
    w.append(float(line[2]))
print("Input in dictionary format is:- " + str(dic))
# print(dic)
sorted_dict = sorting_dict(dic)
print("After sorting :-" + str(sorted_dict))

temp = []
answer = {}
for key, value in sorted_dict.items():
    i = key[0]
    j = key[1]
    if i not in temp:
        if j not in temp:
            temp.append(i)
            temp.append(j)
        else:
            temp.append(i)
        answer[key] = value
    elif i in temp:
        if j not in temp:
            temp.append(j)
            answer[key] = value

print("final answer is:-")
print(answer)
