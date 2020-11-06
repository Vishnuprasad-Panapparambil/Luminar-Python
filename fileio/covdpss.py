fin=open("C:/Users/new/Desktop/complete.csv","r")
i=0
dict={}
list
for lines in fin:
    report=lines.rstrip("\n").split(",")
    state=report[1]
    cured=int(report[6])
    if(state not in dict):
        dict[state]=cured
    else:
        dict[state]=cured
print(dict)
lst=[]
for k,v in dict.items():
    lst.append((v,k))
print(lst)
