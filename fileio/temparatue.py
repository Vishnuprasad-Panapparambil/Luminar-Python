fin=open("C:/Users/new/Desktop/datas.txt","r")
dict={}
temp1=0
data=[]
for line in fin:
    data=line.rstrip("\n").split(",")
    district=data[0]
    temp=int(data[1])

    if((district not in dict)):
        dict[district]=temp

    elif(temp> dict[district]):
        dict[district] = temp
    else:
        pass

print(dict)