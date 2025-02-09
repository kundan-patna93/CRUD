import mysql.connector as cn 


#Establish connection 
conn=cn.connect(
    host="localhost",
    user="root",
    password="123456"
    #database=""
)
print("sucessfull connected" if conn.is_connected() else "Error")
