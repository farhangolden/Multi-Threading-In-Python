import threading
import time

sq=[]
cb=[]

def squares(s,e,a,Name,Version):
    for i in range(s,e):
        print(a,time.ctime(),":",i*i)
        print(Name,Version,sep="\t")
        sq.append(i*i)
        time.sleep(1)

def cube(s,e,a,Name,Version,Year):
    for i in range(s,e):
        print(a,time.strftime(" %H:%M:%S --"),":",i*i*i)
        print(Name,Version,Year,sep="\t")
        cb.append(i*i*i)
        
        time.sleep(2)

t1=threading.Thread(target=squares,args=(1,3,"Squares"),kwargs={"Name":"Threade1","Version":1.25})
t2=threading.Thread(target=cube,args=(2,5,"Cubes"),kwargs={"Name":"Threade2","Version":2.25,"Year":2025})

t1.start()
t2.start()

t1.join()
t2.join()

print(sq)
print(cb)