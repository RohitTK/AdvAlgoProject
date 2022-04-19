
from turtle import update


def sorting_dict(dict_data): 
    return dict(sorted(dict_data.items(), key= lambda x:x[1], reverse= True))
#above method is taken as reference from https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.php 


input_lines=[]
w=[]
edge_list=[]
dic={}
with open('input1.txt') as f:
    input_lines=f.readlines()

for line in input_lines:
    # print(line)
    line=line.split(" ")
    # print(line)
    temp=(int(line[0]),int(line[1]))
    dic[temp]= float(line[2])
    edge_list.append(temp)
    w.append(float(line[2]))


# Reading required vertices from file
with open('required_vertices.txt') as f:
    input_req_vert=f.readlines()

# No need of below for loop
for i in input_req_vert:
    req_vertices=i.split(" ")
req_vertices_updated=[]
for i in req_vertices:
    req_vertices_updated.append(int(i))
# for i in input_req_vert:
#     req_vertices.append(i)


print("Input in dictionary format is:- "+str(dic))
# print(dic)
sorted_dict=sorting_dict(dic)
print("After sorting :-"+str(sorted_dict))

print("Required Vertices are:"+str(req_vertices_updated))

#temp to check whether we visited the vertex or not
temp=[]
answer={}
for key,value in sorted_dict.items():
    i=key[0]
    j=key[1]
    if i in req_vertices_updated and j in req_vertices_updated:
        if j not in temp and i not in temp:
            temp.append(i)
            temp.append(j)
            answer[key]=value
            
        elif j not in temp or i not in temp:
            if i not in temp:
                temp.append(i)
            elif j not in temp:
                temp.append(j)
            answer[key]=value
    else:
        if i in req_vertices_updated or j in req_vertices_updated:
            if i not in temp:
                temp.append(i)
            elif j not in temp:
                temp.append(j)
            answer[key]=value

    req_vertices.sort()
    # breaking the loop, if required vertices are equals to length
    if(temp==req_vertices):
        print("breaking")
        break

print(answer)