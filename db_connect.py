# db_connect.py
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

def connect_to_db():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS")
        )
        print("Connected to the database successfully!")
        return conn
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    connect_to_db()
