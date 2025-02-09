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
        self.lst=[]
        for v in val:
            for v1 in v:
                self.lst.append(v1)
        print(self.lst)

    #Create a new database
    def create_database(self,db_name):
        crud.show_all_database()
        
        if db_name in self.lst:
            print("\n\nThis name_db use database-------"*3)
        else:
            query=(f"CREATE DATABASE {db_name}")
            print("your database sucessfully create")
            obj.execute(query)
        #crud.show_all_database()
            
crud=CRUD_Operation()
#crud.show_all_database()
crud.create_database('kkdb')




# def show_all_database():
#     query="SHOW DATABASES"
#     obj.execute(query)
#     return obj.fetchall()
# val=show_all_database()
# print(val)

