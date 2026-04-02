import psycopg2
import logging
from dotenv import load_dotenv
import os

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.executors.pool import ThreadPoolExecutor

# ---------------- LOGGING ----------------

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

handler.setFormatter(formatter)
logger.addHandler(handler)

# ---------------- DATABASE ----------------

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

# Track previous count
previous_post_count = 0

# ---------------- TASK FUNCTION ----------------

def report_summary():

    global previous_post_count

    try:

        # total users
        cur.execute(
            "SELECT COUNT(DISTINCT user_id) FROM api_schema.posts"
        )
        total_users = cur.fetchone()[0]

        # total posts
        cur.execute(
            "SELECT COUNT(*) FROM api_schema.posts"
        )
        total_posts = cur.fetchone()[0]
        
        conn.commit()
        # new posts since last run
        new_posts = total_posts - previous_post_count

        previous_post_count = total_posts

        logger.info("------ SUMMARY REPORT ------")
        logger.info(f"Total Users : {total_users}")
        logger.info(f"Total Posts : {total_posts}")
        logger.info(f"New Posts Added : {new_posts}")
        logger.info("----------------------------")

    except Exception as e:
        logger.error(f"Monitoring error: {e}")

# ---------------- SCHEDULER ----------------

executors = {
    "default": ThreadPoolExecutor(2)
}

scheduler = BlockingScheduler(executors=executors)

scheduler.add_job(
    report_summary,
    "interval",
    minutes=11,   # slightly slower than task3
    id="summary_report_job"
)

logger.info("Task4 monitoring scheduler started")

scheduler.start()
