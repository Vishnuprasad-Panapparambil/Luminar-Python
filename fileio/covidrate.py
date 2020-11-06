fin=open("C:/Users/new/Desktop/complete.csv","r")
dict={}
a=0
for lines in fin:


    data=lines.rstrip("\n").split(",")

    date=data[0]
    state=data[1]
    confirmed=data[4]
    death=data[5]
    cured=data[6]
    if(state not in dict):
        dict[state]={"state":state,"total confirmed":confirmed,"total cured":cured,"total death":death}
    else:
        dict[state]={"state":state,"total confirmed":confirmed,"total cured":cured,"total death":death}
    if(a==2):
        break
    a=a+1


def getvalues(**kwargs):

    for k,v in kwargs.items():
        state=v
        if(state in dict):
            print(dict[state])
        else:
            print("state not exit")
getvalues(state="Kerala")
