# main.py
import requests
from bs4 import BeautifulSoup
import psycopg
import threading
import time
import config

# Database connection details from config.py
DB_HOST = config.DB_HOST
DB_NAME = config.DB_NAME
DB_USER = config.DB_USER
DB_PASSWORD = config.DB_PASSWORD
NUM_THREADS = config.NUM_THREADS
DATABASE_COMMIT_THRESHOLD = config.DATABASE_COMMIT_THRESHOLD


# Function to scrape a single URL
def scrape_url(url, db_conn):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.title.string if soup.title else ""
        content = ' '.join([p.get_text() for p in soup.find_all('p')])
        links = [a['href'] for a in soup.find_all('a', href=True)]

        # Insert data into the database
        with db_conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO pages (url, title, content)
                VALUES (%s, %s, %s)
                """,
                (url, title, content)
            )
            return True, None  # success

        return False, None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return False, str(e)  # Indicate failure
    except Exception as e:
        print(f"Error processing {url}: {e}")
        return False, str(e)


# Main function
def main():
    start_urls = input("Enter URLs to scrape, separated by spaces: ").split()

    try:
        conn = psycopg.connect(host=DB_HOST, database=DB_NAME, user=DB_USER,
                                password=DB_PASSWORD)
        conn.autocommit = False  # Commit changes in batches

        threads = []
        for url in start_urls:
            thread = threading.Thread(target=scrape_url, args=(url, conn))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        conn.commit()
        conn.close()
        print("Scraping complete!")

    except psycopg.Error as e:
        print(f"Database error: {e}")


if __name__ == "__main__":
    main()