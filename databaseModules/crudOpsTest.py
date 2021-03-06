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
     
     def add_row(self,table_name):
          self.obj.myCursor.execute(f"INSERT INTO {table_name} (first_name,last_name,age,gender) VALUES ('Evaluation2222', 'o4',42,'F');")
          self.obj.connection.commit()
          print("row added")

     def update_row(self,table_name,changes,row_id):
          for item in changes.items():
               print(type(item[0]))
               self.obj.myCursor.execute(f"UPDATE {table_name} SET {item[0]} = '{item[1]}' WHERE id = {row_id};")

          self.obj.connection.commit()
          print(f"{row_id} is updated")

     def delete_row(self,table_name,row_id):
          self.obj.myCursor.execute(f"DELETE FROM {table_name} WHERE id={row_id};")
          self.obj.connection.commit()
          print(f"{row_id} row Deleted")

     def clear_table(self,table_name):
          self.obj.myCursor.execute(f"DELETE FROM {table_name};")
          self.obj.connection.commit()
          print(f"{table_name} table cleared")

     def delete_table(self,table_name):
          self.obj.myCursor.execute(f"DROP TABLE {table_name};")
          self.obj.connection.commit()
          print("table deleted")

     def close_connection(self):
          self.obj.exit_database()
          print("connection closed")

     def load_all_data(self):
          self.obj.myCursor.execute(f"SELECT * FROM Patient")
          print(self.obj.myCursor.fetchall())

if __name__ == "__main__":
     obj2  = CrudOps()
     # obj2.create_table()
     # obj2.add_row(table_name='Patient')

     obj2.load_all_data()

     obj2.close_connection()
