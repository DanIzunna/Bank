import mysql.connector
mydb = mysql.connector.connect(user={ your_mysql_user_name },passwd= { your_mysql_password },host="localhost",database ='BANK', auth_plugin= 'mysql_native_password' ) 
cursor = mydb.cursor()

# The commands to connect to the database is in one file for ease of access
