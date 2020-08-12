import MySQLdb

db = MySQLdb.connect("localhost", "root", "", "test_database")  # Open database connection
cursor = db.cursor()  # prepare a cursor object using cursor() method

cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s " % data)

cursor.execute("SELECT * FROM a")
data = cursor.fetchall()
print(data)


db.close()
