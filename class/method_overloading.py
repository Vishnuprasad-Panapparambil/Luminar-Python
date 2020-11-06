class student:

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def sum(self,m1,m2):
        s=m1+m2
        return s

ob=student(50,60)

print(ob.sum(50,60))