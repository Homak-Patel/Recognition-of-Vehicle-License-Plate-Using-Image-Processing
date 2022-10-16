import sqlite3

conn=sqlite3.connect('vehicleData.db')

reg=input("enter :")
cursor=conn.execute("SELECT*FROM vehicleOwner where RegNo is ?",(reg,))
for row in cursor:
    print(type(row[1]))
