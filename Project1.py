import numpy as np
import threading
import mysql.connector
import time

def save_timing(name, start, end):
    with open("log.txt","a") as f:
        f.write(f"{name}={time.strftime('%H:%M:%S', time.localtime(end))}\n")
        f.write(f"{name} THREAD DURATION={end - start:.2f} seconds\n\n")

def read_csv():
    start=time.time()

    data=np.genfromtxt(
        "data.csv",
        delimiter=",",
        dtype=str,
        skip_header=1
    )
    arr=np.array(data,ndmin=2)

    print("--- CSV DATA ---")
    for row in arr:
        print(row)

    time.sleep(1)
    end=time.time()

    print("CSV TIMING =",time.strftime("%H:%M:%S"))
    save_timing("CSV TIMING",start,end)

# t1=threading.Thread(target=read_csv)
# t1.start()
# t1.join()

def change_case():
    start=time.time()

    with open("input.txt","w") as f:
        f.write("hello farhan\npython programming")

    with open("input.txt","r") as f1:
        data=f1.read().upper()

    with open("output.txt","w") as f2:
        f2.write(data)
    print("--- THIS IS CHANGE CASE ---")
    print(data)

    time.sleep(2)
    end=time.time()

    print("CAPITAL LETTER TIMING =",time.strftime("%H:%M:%S"))
    save_timing("CAPITAL LETTER TIMING",start,end)

# t2=threading.Thread(target=change_case)
# t2.start()
# t2.join()

def read_mysql():
    start=time.time()

    con=mysql.connector.connect(
        host="localhost",
        user="root",
        password="bismillah",
        database="school"
    )

    cur=con.cursor()
    cur.execute("SELECT * FROM students")

    print("--- MySQL DATA ---")

    for row in cur.fetchall():
        print(row)

    time.sleep(3)
    end = time.time()

    print("MYSQL TIMING =", time.strftime("%H:%M:%S"))
    save_timing("MYSQL TIMING",start,end)

    cur.close()
    con.close()

# Clear old timing data
with open("log.txt","w") as f:
    f.write("--- THREAD TIMING REPORT ---\n\n")

t1=threading.Thread(target=read_csv)
t1.start()
t1.join()

t2=threading.Thread(target=change_case)
t2.start()
t2.join()

t3=threading.Thread(target=read_mysql)
t3.start()
t3.join()

print("ALL THREAD TIMINGS SAVED IN timing.txt")