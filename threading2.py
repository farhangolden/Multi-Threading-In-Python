import time
import threading

def Display():
    l1=[5,4,4,8,5,6,7,9,5,9,9]
    for i in l1:
        print("Display",i)
        time.sleep(2)

def sum():
    l1=[5,4,4,8,5,6,7,9,5,9,9]
    s=0
    for i in l1:
        s+=i
        print("Sum",i)
        time.sleep(2)

def StringF():
    str="PythonThread"
    s=[]
    for i in str:
        s.append(i)
        print("String",s)
        time.sleep(2)

t1=threading.Thread(target=Display)
t2=threading.Thread(target=sum)
t3=threading.Thread(target=StringF)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()