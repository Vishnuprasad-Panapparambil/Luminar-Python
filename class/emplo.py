class employi:
    def datas(self,id,desig):
        self.id=id
        self.desig=desig
    def __str__(self):
        return str(self.id)

        #return self.desig
ob=employi()
ob.datas(id=100,desig="dop")
print(ob)
