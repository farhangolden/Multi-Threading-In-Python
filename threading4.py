import threading
import time
import os

def file_read_write(file1,file2):
    os.chdir("D:\\Contends")
    # print(os.getcwd())

    mydata=""
    with open(file1,"r") as f1:
        mydata=f1.read()
        print(mydata)
        f1.close()

    os.chdir("D:\\Farhan Python\\Multi Threading")
    with open(file2,"w") as f2:
        f2.write(mydata)
        f2.close()

    print(time.strftime("%H:%M:%S"))

t1=threading.Thread(target=file_read_write,args=("employees.txt","new_employees.txt"))
t1.start()
t1.join()