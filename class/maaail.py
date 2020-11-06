import re
mail='vishnu@gmail.com'
x='[\w]*@gmail.com'
check=re.fullmatch(x,mail)
if(check==None):
    print("invalid")
else:
    print(mail)
