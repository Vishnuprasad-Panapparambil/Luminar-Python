class product:
    def __init__(self,id,name,category,price):
        self.id=id
        self.name=name
        self.category=category
        self.price=price

    def __str__(self):
        return self.name

lst=[]
ob=lst.append(product(100,"lux","soap",20))
ob=lst.append(product(100,"lux","soap",20))