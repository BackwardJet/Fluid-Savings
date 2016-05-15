import sqlite3

connection = sqlite3.connect(host="192.168.1.167")

c = connection.cursor()
print("Connection Success")
