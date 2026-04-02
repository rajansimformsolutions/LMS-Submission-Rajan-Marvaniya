import requests as rs
import logging

# Configure logging
logging.basicConfig(
    filename="api_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

url = "https://jsonplaceholder.typicode.com/end-point"

try:
    response = rs.get(url, timeout=5)

    # Check HTTP status
    response.raise_for_status()

    data = response.json()
    print(data)

except rs.exceptions.HTTPError as e:
    logger.error(f"HTTP error occurred: {e}")

except rs.exceptions.ConnectionError as e:
    logger.error(f"Connection error occurred: {e}")

except rs.exceptions.Timeout as e:
    logger.error(f"Request timed out: {e}")

except rs.exceptions.RequestException as e:
    logger.error(f"General request error: {e}")

