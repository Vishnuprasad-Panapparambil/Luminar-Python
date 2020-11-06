dict={101:{"name":"vishnu","desig":"developer","salary":15000},102:{"name":"yedhu","desig":"analyst","salary":15000},103:{"name":"anu","desig":"analyst","salary":20000}}
lst=[]
for k,v  in dict.items():
    v["exp"]=2
    if (v["salary"]>18000):
        v["salary"]+=5000
    else:
        v["salary"]+=3000


    print(k,":",v)
print(lst)