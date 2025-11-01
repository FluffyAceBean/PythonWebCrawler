# export.py
import psycopg
import csv
import config

# Database credentials from config.py
DB_HOST = config.DB_HOST
DB_NAME = config.DB_NAME
DB_USER = config.DB_USER
DB_PASSWORD = config.DB_PASSWORD

def export_database():
    """
    Connects to the PostgreSQL database, queries the data, and exports it to a CSV file.
    """
    try:
        conn = psycopg.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
        cur = conn.cursor()

        # Query to retrieve data from the pages table (adjust as needed)
        query = """
            SELECT id, url, title, content
        """
        cur.execute(query)

        # Fetch all results
        rows = cur.fetchall()

        # Define CSV file name
        csv_file = "exported_data.csv"

        # Write data to CSV file
        with open(csv_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)

            # Write header row (optional)
            writer.writerow(['ID', 'URL', 'Title', 'Content'])

            # Write data rows
            writer.writerows(rows)

        print(f"Data exported to {csv_file}")

        cur.close()
        conn.close()

    except psycopg.Error as e:
        print(f"Error connecting to database or exporting data: {e}")


if __name__ == "__main__":
    export_database()