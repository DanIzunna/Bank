# display records before inserting
mycursor.execute("Select * from geeksfoegeeks")
myresult = mycursor.fetchall()
for i in myresult:
	print(i)

	
# statement to insert record
mycursor.execute(
	"Insert into geeksfoegeeks(name,address,age,mob_number,ID_NO) \
	select * from( Select 'Thomas','UK',30,1892345670,'IND100') as temp \
	where not exists \
	(Select ID_NO from geeksfoegeeks where ID_NO='IND100') LIMIT 1")
print("After inserting a record....")


# print records after insertion
mycursor.execute("Select * from geeksfoegeeks")
myresult = mycursor.fetchall()
for i in myresult:
	print(i)
mycursor.execute("Commit")


# close connection
connection.close()
