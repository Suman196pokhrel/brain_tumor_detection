import connector_01

PATIENT = "CREATE TABLE Patient(id INT AUTO_INCREMENT PRIMARY KEY,first_name varchar(14) NOT NULL,last_name varchar(16) NOT NULL,age int NOT NULL,gender enum('M','F') NOT NULL);"

class CrudOps:
     def __init__(self):
          try:
               self.obj =  connector_01.CustomConnector()
               print("Connection Established")
          except Exception:
               print(Exception)     

     def create_table(self):
          self.obj.myCursor.execute(PATIENT)
          print("table created")
     
     def add_row(self):
          self.obj.myCursor.execute(f"INSERT INTO patient (first_name,last_name,age,gender) VALUES ('Suman', 'pokhrel',22,'M');")
          self.obj.connection.commit()
          print("row added")

     def delete_table(self,table_name):
          self.obj.myCursor.execute(f"DROP TABLE {table_name};")
          self.obj.connection.commit()

     def close_connection(self):
          self.obj.exit_database()



if __name__ == "__main__":
     obj2  = CrudOps()
     # obj2.create_table()
     # obj2.add_row()
     obj2.delete_table('patient')


     obj2.close_connection()
