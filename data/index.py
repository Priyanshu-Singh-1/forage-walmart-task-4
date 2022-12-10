
# Creating a database
from pathlib import Path
Path('my_data.db').touch()

# Creating a database to connect with the sqlite
import sqlite3

# Declared the connection as conn
conn = sqlite3.connect('my_data.db')
c = conn.cursor()

# This is the command to create a new table, for this cmd line, I have made a table for loading the 
# data for shipping_data_0
#c.execute('''CREATE TABLE dataOf0 (origin_warehouse varchar, destination_store varchar, product text, on_time text, product_quantity int, driver_identifier varchar)''')

# Importing pandas for reading the file
import pandas as pd

# Reading the file from the csv file
users = pd.read_csv('C:\\Users\\DELL\\Documents\\GitHub\\forage-walmart-task-4\\data\\shipping_data_0.csv')

# write the data to a sqlite table
users.to_sql('dataOf0', conn, if_exists='append', index = False)


#Creating table for storing data 1 and data 2

# --------------------DATA 1-------------------------------
#c.execute('''CREATE TABLE dataOf1 (shipment_identifier varchar, product text, on_time text)''')
user1 = pd.read_csv('C:\\Users\\DELL\\Documents\\GitHub\\forage-walmart-task-4\\data\\shipping_data_1.csv')
user1.to_sql('dataOf1', conn, if_exists='append', index = False)


#---------------------DATA 2--------------------------------
#c.execute('''CREATE TABLE dataOf2 (shipment_identifier varchar, origin_warehouse varchar, destination_store varchar, driver_identifier varchar)''')
user2 = pd.read_csv('C:\\Users\\DELL\\Documents\\GitHub\\forage-walmart-task-4\\data\\shipping_data_2.csv')
user2.to_sql('dataOf2', conn, if_exists='append', index = False)


#-------------------- DATA 3---------------------------------
#This will be the table that will store the information of both the table1 and table2

#Query for having same shipment_identifier
query = """SELECT dataOf1.shipment_identifier, dataOf1.product, dataOf1.on_time, dataOf2.origin_warehouse, dataOf2.destination_store, dataOf2.driver_identifier FROM dataOf1 INNER JOIN dataOf2 on dataOf1.shipment_identifier = dataOf2.shipment_identifier"""

#Writing in CSV file
fields = ['shipment_identifier', 'product', 'on_time', 'origin_warehouse', 'destination_store', 'driver_identifier'] 
ans = c.execute(query)

import csv

# Storing the file in data3.csv file
filename =  "data3.csv"
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(ans)




