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
		query = 'SELECT * FROM ' + self.tableNameUsage		
		c.execute(query)
		for row in c.fetchall():
			print(row[0])

	def UpdateUsage(self,username,amount):
		cursor = self.connection.cursor()
		query = ("UPDATE " + str(self.tableNameUsage) + " SET waterusage = " + str(amount) +  " WHERE username = '" + str(username)+"'")
		#data = (amount,username)
		print(query)
		#cursor.execute(query,data)
		cursor.execute(query)
		self.connection.commit()
		cursor.close()
	
	def printAllUsersUsage(self):
		c = self.connection.cursor()
		query = 'SELECT * FROM ' + self.tableNameUsage
		c.execute(query)
		for row in c.fetchall():
			print(row)

database = Database(login_user,login_password)
database.printAllUsersUsage()
database.UpdateUsage("tejvuligonda@gmail.com",250)
#database.UpdateUsage("test",2)
database.printAllUsersUsage()
