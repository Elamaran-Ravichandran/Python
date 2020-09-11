import pymysql
import pathlib

# user needs to give database name as input
db = input("Please enter the database name that u want to extract all table data : ")
print("Thank you ! File extraction started")

# open a database connection be sure to change the host IP address, username, password and database name to match your info
connection = pymysql.connect ("localhost","root","root",db)

# prepare a cursor object using cursor() method
cursor = connection.cursor()

# execute the SQL query using execute() method.
cursor.execute ("show tables")

# fetch all of the rows from the query
data = cursor.fetchall ()

#converting data(tuple) to all tables (list)
all_tables = [item for t in data for item in t]
# print(all_tables)

# defining output path with pathlib library
output_path = str(pathlib.Path.cwd()/"db_output")

# writing all table in data with table name as file name
for current_tbl in all_tables:
    cursor.execute("select * from " + current_tbl)
    current_tbl_data = cursor.fetchall()

    # write all files as text file
    with open(output_path+"/"+current_tbl+".txt",'w') as db_to_file:
        db_to_file.write(str(current_tbl_data))

    print("data extraction for '"+current_tbl + "' table has been completed"+'\n')

