fin=open("C:/Users/new/PycharmProject/luminartechnolab/venv/my_works/my_work_dictionary/movies.csv","r")
f1=open("C:/Users/new/PycharmProject/luminartechnolab/venv/my_works/my_work_dictionary/movies_append","a")
count=0

for line in fin:
    if (count==100):
        break
    data=line.rstrip("\n").split(",")
    name=data[1]
    rating=float(data[3])
    if (rating>=3.5):
        f1.write(name)
        f1.write("\n")
    else:
        pass
    count+=1



