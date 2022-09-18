import mysql.connector as dbconn

# connect() methods expects 4 parameters
# host - where the DB is hosted or mySQL server is hosted we could say
# database - DB name | one server can host multiple DB's that is the reason you have to give name
# username and pwd - to connect to server
# Python will automatically create a connection string based on all the info we provided
connObject = dbconn.connect(host='localhost', database='APIDevelop', user='root',
                            password='root$')
# print(connObject.is_connected())
if connObject.is_connected():
    print("connected successfully @ localhost DB")
    # To hit or execute any queries or to form the streamline we have to use the cursor object,
    # which we create using connection object
    cursor = connObject.cursor()  # cursor() method is used to establish the steamlined connection to talk to DB tales
    cursor.execute("select * from Books")
    first_row = cursor.fetchone()  # returns first record as tuple
    print(first_row)
    print("3rd coloumn value - ", first_row[3])
    allrecords = cursor.fetchall()  # fetchall - it will return list of tuples, each tuple is a record.
    print(allrecords)
else:
    print("connection failed!")
