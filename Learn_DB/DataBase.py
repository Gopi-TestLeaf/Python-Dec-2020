# Install sqlite3 - pip install db-sqlite3
import sqlite3

# Create Connection
con = sqlite3.connect('database.db')
print('Create DB')
#**************************************************************************************************************
# Create table in database

# CREATE TABLE leaf_db(fName, lName, email, password)
con.execute('''CREATE TABLE IF NOT EXISTS leaf_db(fName, lName, email, password) ''')
print('Table Created')
#**************************************************************************************************************
# Insert the records
con.execute(''' INSERT INTO leaf_db(fName, lName, email, password) 
                VALUES('Babu', 'Manickam', 'babu@gmail.com', '221133')''')
con.commit()
print('Inserting records')
#**************************************************************************************************************
# Update the records
qr = '''UPDATE leaf_db set fName = 'Gopi' WHERE lName='Jayakumar' '''
con.execute(qr)
con.commit()
print('Updated the records')
#**************************************************************************************************************
# fetch all data's
data = con.execute('''SELECT * FROM leaf_db ''')
print(data)

for i in data:
    print(i)

#**************************************************************************************************************
# close the connection
con.close()
print('Close DB')