from threading import *
class mythread(thread):
    def run(self):
        for i in range(10):
            print("inside mythread")
