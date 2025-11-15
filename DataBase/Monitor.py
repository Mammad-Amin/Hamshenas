import sqlite3


db_path = 'HamShenas.db'


conn = sqlite3.connect(db_path)
cursor = conn.cursor()


cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()


print("Tables in the database:")
for table in tables:
    print(table[0])


for table in tables:
    table_name = table[0]
    print(f"\nData in table '{table_name}':")
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    
    # Get column names
    column_names = [description[0] for description in cursor.description]
    print(column_names)
    
    # Print rows
    for row in rows:
        print(row)


conn.close()
