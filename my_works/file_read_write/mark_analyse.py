f=open("C:/Users/new/PycharmProject/luminartechnolab/venv/my_works/my_work_dictionary/marks.csv","r")
f1=open("C:/Users/new//PycharmProject/luminartechnolab/venv/my_works/my_work_dictionary/dictionary_print.py","w")
dict={}
for line in f:
    data=line.rstrip("\n").split(",")
    sub = data[2]


    marks=int(data[3])
    name=data[1]
    if(marks>=55):
        f1.write(name)
        f1.write("\n")
    else:
        pass
    if sub not in dict:
        dict[sub]=1
    else:
        dict[sub]+=1
