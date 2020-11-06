dict={"1":"vishnu","2":"yedhu","3":"anu","4":"madhu"}
dict1={}
for k,v in dict.items():
    if(k,v) not in dict1.items():
        dict1[v]=k
    else:
        pass
print(dict)
print(dict1)