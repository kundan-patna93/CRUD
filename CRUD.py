import mysql.connector as cn 


#Establish connection 
conn=cn.connect(
    host="localhost",
    user="root",
    password="123456",
    database="novodaya_vidayalaya"
)
obj=conn.cursor()
print("sucessfull connected" if conn.is_connected() else "Error")

class CRUD_Operation:

    #fetch all database 
    def show_all_database(self):
        query="SHOW DATABASES"
        obj.execute(query)
        val=obj.fetchall()
        crud.show_database(val)
    
    #show the all databases
    def show_database(self,val):
        print("List of database: ")
        print("-------------------")
        lst=[]
        for v in val:
            for v1 in v:
                lst.append(v1)
        print(lst)
    
    
    
    
crud=CRUD_Operation()
#crud.show_all_database()
    




# def show_all_database():
#     query="SHOW DATABASES"
#     obj.execute(query)
#     return obj.fetchall()
# val=show_all_database()
# print(val)

