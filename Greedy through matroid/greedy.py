# Take input

# split accordingly

# use dict to store edge as key and weight as value

# sort the dictionary based on weight

# use a temp list to check the added edge to the graph cause a cyclic graph

# compare the edges in list, if not add the non exising edges to the temp and also to the graph

# if both edges are in temp list, it causes cyclic graph. So, shd not be added

# return the list of edges with weight


from collections import OrderedDict
input_lines=[]
w=[]
edge_list=[]
dict={}
with open('input.txt') as f:
    input_lines=f.readlines()

for line in input_lines:
    # print(line)
    line=line.split(" ")
    # print(line)
    temp=(int(line[0]),int(line[1]))
    # temp.append(int(line[0]))
    # temp.append(int(line[1]))
    dict[temp]= float(line[2])
    edge_list.append(temp)
    w.append(float(line[2]))

# print(dict)
dict1=dict(sorted(dict.items(),key=lambda x:x[1], reverse=True))
print(dict1)
# dict1 = OrderedDict(sorted(dict.items())) #inbuilt function for sorting based on the value in dict
# print(dict1)
# dict2= OrderedDict(reversed(dict1))
# print(dict2)

# print("sorted based on weight is "+str(dict2))
# print(type(dict1))
temp=[]
answer=[]
for i,j in dict1:
    if i not in temp:
        if j not in temp:
            temp.append(i)
            temp.append(j)
        else:
            temp.append(i)
        answer.append((i,j))
    elif i in temp:
        if j not in temp:
            temp.append(j)
            answer.append((i,j))

# print(answer)

final_answer={}
for i in answer:
    print(i)
    # final_answer[i]=dict[i]


print(final_answer) #returning final list of edges


# sorted_dict=dict1[0]
# print(sorted_dict)
# count=0
# for line in input_lines:
#     print("Edge: "+str(edge_list[count]))
#     print("Weight of "+str(edge_list[count])+ "is "+str(w[count]))
#     count=count+1

# #sort the edge lists


# use temp as list and add new edges to it like:
# []
# [2,3]
# [2,3,1]
# [2,3,1,0]

# Check every time whether a,b is in List