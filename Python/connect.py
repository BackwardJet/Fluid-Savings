import sqlite3
import MySQLdb

login_user = "sql3119660"
login_password = "SLeidVsdzP"

class Database:
	def __init__(self,login_user,login_password):
		self.connection = MySQLdb.connect(host= "sql3.freemysqlhosting.net",user = login_user, passwd = login_password,db = "sql3119660")
		self.databaseName = "sql3119660"
		self.tableNameUsers = "users"
		self.tableNameUsage = "watermeterusage"
		print ("Connection Sucess")

	def printAllUsers(self):
		c = self.connection.cursor() 		
		c.execute('SELECT * FROM ' + self.tableNameUsage)
		for row in c.fetchall():
			print(row[0])

database = Database(login_user,login_password)
database.printAllUsers()

