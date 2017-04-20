import sqlite3
import random

#establish connection and create newnum.db database
with sqlite3.connect("newnum.db") as connection:
    #open cursor
    c = connection.cursor()

    #create numbers table 
    c.execute("DROP TABLE if exists numbers")
    c.execute("CREATE TABLE numbers(num int)")

    #create 100 random numbers between 1 and 100 and insert into table
    for i in range(100):
        c.execute("INSERT INTO numbers VALUES(?)", (random.randint(0,100),))