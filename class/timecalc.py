import time
from threading import *

def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print("double values=",2*n)
def squares(numbers):
    for n in numbers:
        time.sleep(1)
        print("square values=",n*n)

numbers=[1,2,3,4,5]
begintime=time.time()
t=Thread(target=doubles,args=(numbers,))
t1=Thread(target=squares,args=(numbers,))
t1.start()
t.start()
t.join()
t1.join()
endtime=time.time()
print("Total time taken",endtime-begintime)
