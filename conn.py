import mysql.connector as a
mydb=a.connect(host="localhost",user="root",password="password123")
if(mydb):
    print("connetion successful")
else:
    print("connetion unsuccessful")
