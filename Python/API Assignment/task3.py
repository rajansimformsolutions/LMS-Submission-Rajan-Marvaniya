import requests
import psycopg2
import logging
from dotenv import load_dotenv
import os

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.executors.pool import ThreadPoolExecutor

# ---------------- LOGGING ----------------

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("api_errors.log")
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# ---------------- DATABASE ----------------

from dotenv import load_dotenv
import os
import psycopg2

# load .env file
load_dotenv()

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

logger.info("Connected to database!")
cur = conn.cursor()

# ---------------- TASK FUNCTION ----------------

def fetch_posts():

    try:
        logger.info("Fetching posts from API")

        url = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        posts = response.json()

        inserted = 0

        for post in posts:

            cur.execute(
                """
                INSERT INTO api_schema.posts (id, user_id, title, body)
                VALUES (%s,%s,%s,%s)
                ON CONFLICT (id) DO NOTHING
                """,
                (post["id"], post["userId"], post["title"], post["body"])
            )

            if cur.rowcount > 0:
                inserted += 1

        conn.commit()

        logger.info(f"{inserted} new posts inserted into database")

    except Exception as e:

        logger.error(f"Error during API task: {e}")

# ---------------- SCHEDULER ----------------

executors = {
    "default": ThreadPoolExecutor(5)
}

scheduler = BlockingScheduler(executors=executors)

scheduler.add_job(
    fetch_posts,
    "interval",
    minutes=10,
    id="fetch_posts_job"
)

logger.info("Scheduler started. Running every 10 minutes")

scheduler.start()