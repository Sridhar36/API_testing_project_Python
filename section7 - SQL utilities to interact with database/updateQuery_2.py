import mysql.connector as dbconn

connObject = dbconn.connect(host='localhost', database='APIDevelop', user='root',
                            password='root$')
if connObject.is_connected():
    print("connected successfully @ localhost DB")
    cursor = connObject.cursor()  # cursor() method is used to establish the steamlined connection to talk to DB tales
    query = "update customerInfo set Location = %s where CourseName = %s "
    data = ('POK', 'Jmeter')
    cursor.execute(query, data)
    # once you update, you have to commit. After update you have to run commit
    # Commit has to be done at connection level
    connObject.commit()
else:
    print("connection failed!")
