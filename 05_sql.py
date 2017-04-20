#INSERT Command with Error Handler
#import sys
# import the sqlite library
import sqlite3

# create the connection object
conn = sqlite3.connect("new.db")

# get a cursor object used to excute SQL commands
cursor = conn.cursor()

try:
    # insert data
    cursor.execute("INSERT INTO populations VALUES('New York City', 'NY', 8400000)")
    cursor.execute("INSERT INTO populations VALUES('San Francisco', 'CA', 800000)")

    # commit the changes
    conn.commit()
except sqlite3.OperationalError:
    #e = sys.exc_info() [0]
    print(e)
    print("Oops!  Something went wrong.  Try again...")
    #print("Error: " & e)

# close the database connection
conn.close()