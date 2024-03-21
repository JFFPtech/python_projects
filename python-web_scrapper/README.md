# Web Scraping Application

This Python script/application allows you to scrape data from websites and store it in a structured format. It includes features such as scheduling, data cleaning, error handling, logging, MySQL integration, and configuration file usage.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- BeautifulSoup (`beautifulsoup4`) module (can be installed via pip)
- Pandas module (can be installed via pip)
- Requests module (can be installed via pip)
- APScheduler module (can be installed via pip)
- MySQL Connector module (can be installed via pip)

## Installation

To install the required dependencies, run the following command:

```
pip install beautifulsoup4 pandas requests apscheduler
```

## Usage

1. Open the `web_scraping.py` script in a text editor.
2. Update the following variables with your own information:
   - `URL`: Set this to the URL of the website you want to scrape.
   - `output_file`: Set this to the desired filename/path for storing the scraped data (e.g., CSV, JSON, or database).
   - `schedule_interval`: Set this to the desired interval for scraping data (e.g., 'hourly', 'daily', etc.).
3. Customize the scraping logic in the `scrape_wikipedia_page()` function to extract the desired data from the website.
4. Set up MySQL database configuration in `mysql_config.json`.
5. Run the script using the following command:

```
python script_name.py <Wikipedia_URL> <output_file_name.csv>

```

## Features

- **Scheduling**: Automatically scrape data at specified intervals using the APScheduler library.
- **Data Cleaning**: Implement data cleaning and transformation logic as needed within the `scrape_wikipedia_page()` function.
- **Error Handling**: Handle errors gracefully using try-except blocks and logging to ensure robustness.
- **Logging**: Logs are written to a file named `scraping.log`, with logging levels INFO and ERROR.
- **MySQL Integration**: Store scraped data in a MySQL database.
- **Configuration Files**: Utilize JSON configuration files to manage parameters such as URL, output file name, and MySQL database credentials.

## Customization

You can customize the scraping logic, error handling, and data processing steps according to the structure and content of the website you are scraping.

## Acknowledgements

- This project was inspired by the need to automate the process of scraping data from websites.
- Special thanks to the developers of BeautifulSoup, Pandas, Requests, APScheduler, and MySQL Connector for providing the tools necessary for web scraping, scheduling, and database integration in Python.