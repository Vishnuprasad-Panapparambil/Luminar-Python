class employee:
    def __init__(self,id,name,desig,mailid,salary):
        self.id=id
        self.name=name
        self.desig=desig
        self.mailid=mailid
        self.salary=salary

    def __str__(self):
        return self.name
        return self.salary





fin=open("C:/Users/new/PycharmProject/luminartechnolab/venv/class/emplodata")
lst=[]
l1=[]
for line in fin:
    data = line.rstrip("\n").split(",")
    ob = employee(data[0], data[1], data[2], data[3], int(data[4]))
    lst.append(ob)
    l1.append(ob.salary)
    print(ob)

print("maximum salary is",max(l1))
print(l1)






