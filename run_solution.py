import mysql.connector
from getpass import getpass

solution_files = [
    "SQL-Challenge/Problem1/solution1.sql",
    "SQL-Challenge/Problem2/solution2.sql",
    "SQL-Challenge/Problem3/solution3.sql",
    "SQL-Challenge/Problem4/solution4.sql",
    "SQL-Challenge/Problem5/solution5.sql",
]

password = getpass("Enter MySQL password: ")
for path in solution_files:
    print(f"\n{'='*50}")
    print(f"Running: {path}")
    print(f"{'='*50}")

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,  # change this
        database="solution"
    )
    cursor = conn.cursor()

    with open(path, "r") as f:
        sql = f.read()

    # Split into individual statements and run one by one
    statements = [s.strip() for s in sql.split(";") if s.strip()]

    try:
        for statement in statements:
            cursor.execute(statement)
            
            # If it returns rows, print them
            if cursor.description:
                rows = cursor.fetchall()
                headers = [desc[0] for desc in cursor.description]
                print(" | ".join(headers))
                print("-" * 50)
                for row in rows:
                    print(" | ".join(str(val) for val in row))

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()

print("\nAll solutions executed!")