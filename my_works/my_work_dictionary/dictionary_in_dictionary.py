dict={101:{"name":"vishnu","desig":"developer"},102:{"name":"yedhu","desig":"analyst"},103:{"name":"anu","desig":"analyst"}}
print(dict)
dict1={}
lst=[]
for k,v in dict.items():
    dict1=v
    lst.append(v)
print(dict1)
print(lst)