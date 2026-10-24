import mysql.connector
import threading

def read_mysql():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="bismillah"
    )

    cur = con.cursor()

    cur.execute("CREATE DATABASE IF NOT EXISTS school")
    cur.execute("USE school")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT,
            name VARCHAR(50),
            age INT
        )
    """)

    cur.execute("DELETE FROM students")

    cur.executemany("""
        INSERT INTO students (id, name, age)
        VALUES (%s, %s, %s)
    """, [
        (1, "Farhan", 17),
        (2, "Ali", 18),
        (3, "Rahul", 16),
        (4, "Aman", 17),
        (5, "Rohit", 19),
        (6, "Sameer", 18),
        (7, "Arman", 17),
        (8, "Rehan", 16),
        (9, "Zaid", 18),
        (10, "Adil", 19),
        (11, "Sahil", 17),
        (12, "Faiz", 18),
        (13, "Imran", 20),
        (14, "Ayaan", 16),
        (15, "Irfan", 19)
    ])

    con.commit()

    cur.execute("SELECT * FROM students")

    for row in cur.fetchall():
        print(row)

    cur.close()
    con.close()

t = threading.Thread(target=read_mysql)
t.start()
t.join()