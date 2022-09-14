import mysql.connector
mydb = mysql.connector.connect(user="Jon",passwd="ilikecheeseballs2",host="localhost",database ='BANK', auth_plugin= 'mysql_native_password' ) 
cursor = mydb.cursor() 

data = cursor.fetchall()
for i in data:
    print('\tCustomer %s'%str(i[0]), i[1:3])
# for i in data:
#     print('\tCustomer %s'%str(i[0]))
#     print('\tFirst Name:'+ str(i[1]))
#     print('\tLast Name:'+ str(i[2]))
#     print('\tAge:%s '%str(i[3]))
#     print('\tGender:'+ str(i[4]))
#     print()