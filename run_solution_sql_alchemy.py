from sqlalchemy import create_engine, text
from getpass import getpass

password = getpass("Enter MySQL password: ")
# Connection string format:
# dialect+driver://username:password@host:port/database
engine = create_engine(f"mysql+pymysql://root:{password}@localhost:3306/solution")

# Read a solution file and execute
def run_solution(filepath):
    print(f"\n{'='*50}")
    print(f"Running: {filepath}")
    print(f"{'='*50}")
    
    with open(filepath, "r") as f:
        sql = f.read()
    
    # Split into individual statements
    statements = [s.strip() for s in sql.split(";") if s.strip()]
    
    with engine.connect() as conn:
        for statement in statements:
            try:
                result = conn.execute(text(statement))
                
                # If SELECT, print results
                if result.returns_rows:
                    headers = result.keys()
                    print(" | ".join(headers))
                    print("-" * 50)
                    for row in result:
                        print(" | ".join(str(val) for val in row))
                        
            except Exception as e:
                print(f"Error: {e}")

# Run all solutions
solution_files = [
    "SQL-Challenge/Problem1/solution1.sql",
    "SQL-Challenge/Problem2/solution2.sql",
    "SQL-Challenge/Problem3/solution3.sql",
    "SQL-Challenge/Problem4/solution4.sql",
    "SQL-Challenge/Problem5/solution5.sql",
]

for path in solution_files:
    run_solution(path)

print("\nAll solutions executed!")