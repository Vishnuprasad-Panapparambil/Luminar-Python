word=input("enter the word")
data=list(word)
print(data)
dict={}
for ltr in data:
    if(ltr not in dict):
        dict[ltr]=1
    else:
        print(ltr,"is recursing")
        break