import mysql.connector;

conn=mysql.connector.connect(host='localhost',database='pharma',user='root',password= '1234')

if conn.is_connected():
	print('Connected Successfully to  pharma db')

cursor = conn.cursor()

cursor.execute('select * from Doctor')
row = cursor.fetchone()

while row is not None:
	print(row)
	row=cursor.fetchone()

cursor.close()
conn.close()
