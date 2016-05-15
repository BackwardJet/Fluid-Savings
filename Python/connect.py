import sqlite3
import MySQLdb

connection = MySQLdb.connect(host="192.168.1.167",user="root",passwd="1234",db="anotherone")
#connection = sqlite3.connect("192.168.1.167")

c = connection.cursor()
print("Connection Success")

c.execute('SELECT * FROM users')

for row in c.fetchall():
	print(row)
