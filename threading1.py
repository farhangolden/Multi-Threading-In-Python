import time
import threading

def f1():
    for i in range(5):
        print("Thread 1",i)
        time.sleep(1)

def f2():
    for i in range(5):
        print("Thread 2",i)
        time.sleep(1)

t1=threading.Thread(target=f1)
t2=threading.Thread(target=f2)

t1.start()
t2.start()

t1.join()
t2.join()