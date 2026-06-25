import mysql.connector
import os
from getpass import getpass

password = getpass("Enter MySQL password: ")
# Connect to your MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,  # change this
    database="solution"              # your database name
)

cursor = conn.cursor()

# List of all schema.sql file paths
schema_files = [
    "SQL-Challenge/Problem1/schema1.sql",
    "SQL-Challenge/Problem2/schema2.sql",
    "SQL-Challenge/Problem3/schema3.sql",
    "SQL-Challenge/Problem4/schema4.sql",
    "SQL-Challenge/Problem5/schema5.sql",
]

for path in schema_files:
    print(f"Loading {path}...")
    with open(path, "r") as f:
        sql = f.read()
    
    # Execute each statement one by one
    for statement in sql.split(";"):
        statement = statement.strip()
        if statement:
            try:
                cursor.execute(statement)
            except Exception as e:
                print(f"  Skipped: {e}")

conn.commit()
cursor.close()
conn.close()
print("All schemas loaded successfully!")  