class product:
    def __init__(self,id,name,category,price):
        self.id=id
        self.name=name
        self.category=category
        self.price=price

    def __str__(self):
        return self.name



lst=[]
sqlst=[]
ob=lst.append(product(100,"lux","soap",20))
ob=lst.append(product(101,"colgate","paste",50))
ob=lst.append(product(100,"nike","shoe",1000))
for item in lst:
    print (item)
sqlst=list(map(lambda product:product.name.upper(),lst))
print(sqlst)
price=list(filter(lambda product:product.price>50,lst))
for value in price:
    print(value)
