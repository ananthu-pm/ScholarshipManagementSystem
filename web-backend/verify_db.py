from database import select, database

try:
    print(f"Testing connection to database '{database}'...")
    # Just try to connect and execute a simple query. 
    # Even if table doesn't exist, we want to see if auth fails.
    # We can try selecting 1.
    res = select("SELECT 1")
    print("Connection Successful!")
    print("Result:", res)
except Exception as e:
    print("Connection Failed!")
    print(e)
