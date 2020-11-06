import re
x='[a-zA-Z0-9]*@gmail.com'
f=open("C:/Users/new/PycharmProject/luminartechnolab/class/emplodata","r")
for line in f:
    datas=line.split(",")
    mailid=(datas[3])
    check=re.fullmatch(x,mailid)
    if (check==None):
        print(mailid,"is","invalid")
    else:
        f1=open("C:/Users/new/PycharmProject/luminartechnolab/class/validmails","a")
        f1.write(mailid)
        f1.write("\n")
