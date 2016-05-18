import sqlite3
import MySQLdb

login_user = "sql3119660"
login_password = "SLeidVsdzP"

connection = MySQLdb.connect(host="sql3.freemysqlhosting.net",user="sql3119660",passwd="SLeidVsdzP",db="sql3119660")
#connection = sqlite3.connect("192.168.1.167")

c = connection.cursor()
print("Connection Success")

c.execute('SELECT * FROM users')

for row in c.fetchall():
	print(row)

class Database:
	def __init__(self,login_user,login_password):
		self.connection = MySQLdb.connect(host= "sql3.freemysqlhosting.net",user = login_user, passwd = login_password,db = "sql3119660")
		self.databaseName = "sql3119660"
		self.tableNameUsers = "users"
		self.tableNameUsage = "watermeterusage"
		print ("Connection Sucess")
		

database = Database(login_user,login_password)


