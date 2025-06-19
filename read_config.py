import yaml

# Load the config.yaml file
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Print database settings
db = config['database']
print("Database Host:", db['host'])
print("Database User:", db['username'])
print("Database Name:", db['dbname'])

# Print service settings
service = config['service']
print("Service starts at:", service['start_time'])
print("Retries allowed:", service['retries'])

import psycopg2

try:
    # Connect to PostgreSQL using values from config.yaml
    conn = psycopg2.connect(
        host=db['host'],
        port=db['port'],
        user=db['username'],
        password=db['password'],
        dbname=db['dbname']
    )
    print("✅ Successfully connected to PostgreSQL RDS")

    # Optional: run a test query
    cur = conn.cursor()
    cur.execute("SELECT version();")
    version = cur.fetchone()
    print("PostgreSQL version:", version[0])

    cur.close()
    conn.close()

except Exception as e:
    print("❌ Error connecting to PostgreSQL:", e)
