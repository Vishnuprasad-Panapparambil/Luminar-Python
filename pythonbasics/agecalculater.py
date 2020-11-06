d=int(input("entner b date"))
m=int(input("entner b mnt"))
y=int(input("entner b year"))
d1=int(input("entner c date"))
m1=int(input("entner c mnt"))
y1=int(input("entner c year"))

year=y1-y
month=m1-m
date=d1-d
if(m1<m):
    year=year-1
print("age","=",year,"month","=",month)