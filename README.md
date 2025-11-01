# Web Scraper

A Python script designed to scrape web pages, extract data (title, content, links), store it in a PostgreSQL database, and export the database for easier analysis and visualization.

## Prerequisites

*   Python 3.6+
*   PostgreSQL database (e.g., using Docker or a local installation)
*   Required Libraries: `requests`, `beautifulsoup4`, `psycopg2`, `rich` (for database export).  Consider using a virtual environment to manage dependencies.

## Installation

1.  **Clone the Repository:**

    ```bash
    git clone [repository URL]
    ```

2.  **Install Dependencies:**

    ```bash
    pip install requests beautifulsoup4 psycopg rich
    ```

3.  **Configure Database Credentials:**

    *   Create a `config.py` file (if it doesn't exist) and populate it with your PostgreSQL database credentials.  Example:

        ```python
        # config.py
        DB_HOST = "localhost"
        DB_NAME = "yourdatabase"
        DB_USER = "yourusername"
        DB_PASSWORD = "yourpassword"
        NUM_THREADS = 5
        DATABASE_COMMIT_THRESHOLD = 20
        ```

4.  **Set up PostgreSQL:**
    *   Ensure you have a PostgreSQL database set up with the name specified in `config.py`.

## Usage

1.  **Run the Script:**

    ```bash
    python main.py
    ```

2.  **Enter Initial URLs:**  When prompted, enter the starting URLs for scraping, separated by spaces.  These URLs will be the seeds for exploring the web.

## Features

*   **Web Scraping:**  Extracts titles, content, and links from web pages.
*   **Database Storage:**  Stores scraped data in a PostgreSQL database.
*   **Parallel Processing:**  Uses multiple threads to accelerate the scraping process.
*   **Robots.txt Respect:**  Respects `robots.txt` rules to avoid overloading servers and adhere to ethical scraping practices.
*   **Database Export:**  Exports the PostgreSQL data into a human-readable format (e.g., CSV, JSON, or a custom format) for analysis and visualization.
*   **Error Handling:** Includes robust error handling to prevent crashes and provide informative error messages.

## Configuration

*   **`NUM_THREADS`**: Controls the number of threads used for scraping. Higher values increase scraping speed but may impact server load.
*   **`DATABASE_COMMIT_THRESHOLD`**:  Defines how many URLs are scraped before committing changes to the database.
*   **Database Credentials:**  Modify the `config.py` file to reflect your database host, name, user, and password.

## Exporting Database Data (Optional)

To export the data for analysis, use the following command after scraping:

```bash
python export_database.py
```

This script will generate a CSV file (or other chosen format) containing the scraped data from your database.

## Contributing

Feel free to open an issue and a pull request for any issues and improvements related to the code.

### Errors and Improvements

*   **Potential Refinements:** Consider implementing more sophisticated link filtering to avoid scraping irrelevant content.
*   **Rate Limiting:** Add more aggressive rate limiting to prevent getting blocked by target websites.
*   **Proxy Support:** Integrate proxy support for anonymity and bypassing geographic restrictions.
*   **Improved Logging:** Enhance logging for easier debugging and monitoring.

### Disclaimer

This project cannot be used to plagiarize my work into someone else's academic code without prior authorization from my part. Please check your local academic institution's ethics committee for the potential consequences resulting from plagiarizing my work.

However, since this project is under the [GPL-3.0 license](https://www.gnu.org/licenses/gpl-3.0.en.html) and the [Opinionated Queer License (OQL) v1.2](https://oql.avris.it/license?c=FluffyAceBean), inclusion of my code can be redistributed and modified without proper authorization from myself with respect to their license agreements. If any license issue occurs between the GPL-3.0 and the OQL v1.2, the OQL v1.2 should remain superior.

Please contact me or open an issue if needed.

`SPDX-License-Identifier: GPL-3.0 AND LicenseRef-OQL-1.2`
