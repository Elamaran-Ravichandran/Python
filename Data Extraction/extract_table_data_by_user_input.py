import pymysql
import pathlib
# defining output path with pathlib library
output_path = str(pathlib.Path.cwd() / "db_output")
class Extract:
    def __init__(self,host,user,pwd,dbn=''):
        # make dbn as optional variable
        self.host = host
        self.user = user
        self.pwd = pwd
        self.dbn = dbn

    # Function to show the databases
    def show_db(self):
        # open a database connection be sure to change the host IP address, username, password and database name to match your info
        connection = pymysql.connect(self.host, self.user,self.pwd)
        # prepare a cursor object using cursor() method
        cursor = connection.cursor()

        # execute the SQL query using execute() method.
        cursor.execute("show databases")

        # fetch all of the rows from the query
        data_db = cursor.fetchall()
        # converting data(tuple) to all tables (list)
        all_dbs = [item for f in data_db for item in f]

        # Print all_db names
        print("Good News ! connection successful. Now you can select the database name from your schema which you would want to extract the data"+'\n')
        print("The database names are below: " +'\n'+('\n'.join(map(str, all_dbs))+'\t'))
        print('\n')

    # Function to select the database and show the tables
    def select_db(self):
        self.dbn = input("Please enter the database name that u want to extract all table data : ")
        print("Thank you ! You're now connected to "+str(self.dbn)+"database")
        connection = pymysql.connect(self.host, self.user,self.pwd, self.dbn)
        cursor = connection.cursor()
        cursor.execute("show tables")
        data_tables = cursor.fetchall()
        all_tables = [item for t in data_tables for item in t]

        print("The table names from "+self.dbn+" database are below: " +'\n'+('\n'.join(map(str, all_tables))+'\t'))
        print('\n')
        # return connection

    # Function to select a table
    def select_table(self):

        tab = input("Please enter the table name which you would want to extract : ")
        # writing all table in data with table name as file name
        connection = pymysql.connect(self.host, self.user, self.pwd,self.dbn)
        cursor = connection.cursor()
        cursor.execute("select * from " + tab)
        current_tbl_data = cursor.fetchall()

        # write all files as text file
        with open(output_path + "/" + tab + ".txt", 'w') as db_to_file:
            db_to_file.write(str(current_tbl_data))
            print("data extraction for '" + tab + "' table has been completed")

# Initial user inputs to make connection
hostname = input("Please enter the host name : ")
username = input("Please enter the user name : ")
password = input("Please enter the password  : ")
print('\n')
db_task = Extract(hostname,username,password)
db_task.show_db()
db_task.select_db()
db_task.select_table()
