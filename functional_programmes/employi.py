class employi:
    def __init__(self,id,name,designation,salary,experience):
        self.id=id
        self.name=name
        self.designation=designation
        self.salary=salary
        self.experience=experience
    def printvalue(self):
        print(self.id,self.name,self.designation,self.salary,self.experience)

lst=[]
f=open("C:/Users/new/PycharmProject/luminartechnolab/fileio/employidetails")
for line in f:
    data=line.rstrip("\n").split(",")
    ob=employi(data[0],data[1],data[2],int(data[3]),int(data[4]))
    lst.append(ob)
    ob.printvalue()

name_uppercase=list(map(lambda employi:employi.name.upper(),lst))
print("\n",name_uppercase)

salary=list(filter(lambda employi:employi.salary>15000,lst))
print("\n","EMPLOYEES WITH SALARY HIGHER THAN 15000")
for data in salary:
    print(data.name)

increment=list(filter(lambda employi:employi.experience>2,lst))
print("\n","INCREMENTED SALARY")
for data in increment:
    print(data.name,(data.salary+5000))

developers=list(filter(lambda employi:employi.designation=="developer",lst))
print("\n","LIST OF DEVELOPERS")
for data in developers:
    print(data.name)

