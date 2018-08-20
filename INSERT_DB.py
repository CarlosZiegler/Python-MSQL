import pymysql

# Open database connection
db = pymysql.connect("127.0.0.1","root","","TESTDB")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
   LAST_NAME, AGE, SEX, INCOME)
   VALUES ('Carlos', 'Ziegler', 33, 'M', 1984),
   ('Carla', 'Jociane', 28, 'F', 1988)"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()