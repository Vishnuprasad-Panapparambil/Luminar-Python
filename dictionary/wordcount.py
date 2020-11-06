fin=open("C:/Users/new/Desktop/movies.csv","r")
dict={}
i=0
rating=0
for line in fin:
    word=line.rstrip("\n").split(",")
    rating=int(word[3])
    print(rating)
    i+=1
    if(rating>3.5):
        dict=line
        print(dict)
    if(i==2):
        break

