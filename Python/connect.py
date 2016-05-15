import sqlite3
import MySQLdb

connection = MySQLdb.connect(host="192.168.1.167",user="root",passwd="1234",db="test1")
#connection = sqlite3.connect("192.168.1.167")

c = connection.cursor()
print("Connection Success")
