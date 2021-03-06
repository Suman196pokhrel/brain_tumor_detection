# Imports
from dotenv import load_dotenv
import os
import mariadb





# Setting Up middlewares
load_dotenv()  # Loading the environment Variables


class CustomConnector:

	def __init__(self, host_name=os.getenv("HOST"), user_name=os.getenv("USER"), password=os.getenv("PASSWORD"), database_name=os.getenv("DATABASE") ,port_num = int(os.getenv("PORT"))):

		self.connection = mariadb.connect(host=host_name, user=user_name, password=password, database=database_name, port = port_num)
		self.myCursor = self.connection.cursor(buffered=True)
		print('Connection established')

	def execute(self, command):
		self.result = self.myCursor.execute(command)
		print("Command ==>> " + command)
		return self.result

	def exit_database(self):
		self.myCursor.close()
		self.connection.close()
		print("Connection closed")
	



if __name__ == "__main__":
    obj = CustomConnector()
#     obj.execute('SELECT * FROM btd.patient')
    obj.exit_database()

