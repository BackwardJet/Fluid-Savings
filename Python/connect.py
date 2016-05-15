import sqlite3
import MySQLdb

connection = MySQLdb.connect(host="sql3.freemysqlhosting.net",user="sql3119660",passwd="SLeidVsdzP",db="sql3119660")
#connection = sqlite3.connect("192.168.1.167")

c = connection.cursor()
print("Connection Success")

c.execute('SELECT * FROM users')

for row in c.fetchall():
	print(row)
