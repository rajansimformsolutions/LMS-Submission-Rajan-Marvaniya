import psycopg2
import requests
from dotenv import load_dotenv
import os


# Database connection
# read variables
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# connect to database
conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)


cur = conn.cursor()


cur.execute("""
CREATE SCHEMA IF NOT EXISTS api_schema;
""")


cur.execute("""
CREATE TABLE IF NOT EXISTS api_schema.users (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    address TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS api_schema.posts (
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES api_schema.users(id),
    title TEXT,
    body TEXT
)
""")
conn.commit()

users_url = "https://jsonplaceholder.typicode.com/users"
users_data = requests.get(users_url).json()

for user in users_data:
    address = f"{user['address']['street']}, {user['address']['suite']}, {user['address']['city']}, {user['address']['zipcode']}"
    cur.execute("""
        INSERT INTO api_schema.users (id, name, email, address)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING
    """, (user['id'], user['name'], user['email'], address))

conn.commit()
print(f"Inserted {len(users_data)} users (duplicates skipped)")


posts_url = "https://jsonplaceholder.typicode.com/posts"
posts_data = requests.get(posts_url).json()

for post in posts_data:
    cur.execute("""
        INSERT INTO api_schema.posts (id, user_id, title, body)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING
    """, (post['id'], post['userId'], post['title'], post['body']))

conn.commit()
print(f"Inserted {len(posts_data)} posts (duplicates skipped)")


cur.close()
conn.close()