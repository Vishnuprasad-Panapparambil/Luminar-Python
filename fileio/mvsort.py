fin=open("C:/Users/new/Desktop/movies.csv","r")
list1=[]
list2=[]
list3=[]
i=0
for line in fin:
    word=line.rstrip("\n").split(",")
    rate=(word[3])
    rate=float((rate))
    if((rate)>=3.5):
        list1.append(word)
    elif (3.5>(rate) >= 2.5):
        list2.append(word)
    elif ((rate) < 2.5):
        list3.append(word)
    else:
        pass
    i += 1
    if(i==100):
        break
l1=len(list1)
l2=len(list2)
l3=len(list3)
print("movies with rating >=3.5",":",l1,"\n",list1)
print("movies having rating between 3.5 & 2.5",":",l2,"\n",list2)
print("movies with rating <2.5",":",l3,"\n",list3)