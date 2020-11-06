fin=open("C:/Users/new/PycharmProject/luminartechnolab/fileio/file1.py","r")
lst=[]
for name in fin:
    print(name)
    lst.append(name.rstrip("\n"))
print(lst)
for name in lst:
    print (name.upper())