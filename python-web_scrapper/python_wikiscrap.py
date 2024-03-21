import requests
import argparse
import logging
import json
import mysql.connector
from bs4 import BeautifulSoup
import os.path
import pandas as pd

# Configure logging
logging.basicConfig(filename='scraping.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(config_file):
    """
    Load configuration parameters from a JSON file.
    
    Parameters:
        config_file (str): The filename of the JSON configuration file.
    
    Returns:
        dict: A dictionary containing the configuration parameters.
    """
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

def connect_to_mysql(mysql_config_file):
    """
    Connect to MySQL database using credentials from a JSON config file.
    
    Parameters:
        mysql_config_file (str): The filename of the JSON configuration file containing MySQL credentials.
    
    Returns:
        mysql.connector.connection.MySQLConnection: A MySQL database connection object.
    """
    with open(mysql_config_file, 'r') as f:
        mysql_config = json.load(f)
    
    return mysql.connector.connect(
        host=mysql_config['host'],
        user=mysql_config['user'],
        password=mysql_config['password'],
        database=mysql_config['database']
    )

def scrape_wikipedia_page(url):
    """
    Scrape data from a Wikipedia page.
    
    Parameters:
        url (str): The URL of the Wikipedia page to scrape.
    
    Returns:
        list: A list containing the scraped data.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract relevant data from the Wikipedia page
        data = []
        # Example: Extract the text content of all <p> tags within the page's content
        for paragraph in soup.find(id='mw-content-text').find_all('p'):
            data.append(paragraph.get_text())
        
        return data
        
    except requests.exceptions.RequestExceptions as e:
        logging.error("An error occurred while sending the URL request: %s", str(e))
        raise 
    
    except Exception as e:
        logging.error("An error occurred while scraping the Wikipedia page: %s", str(e))
        return []

def save_to_csv(data, output_file):
    """
    Save scraped data to a CSV file.
    
    Parameters:
        data (list): The data to be saved.
        output_file (str): The filename for the output CSV file.
    """
    try:
        # Check if the file exists
        file_exists = os.path.isfile(output_file)

        # If the file exists, append data to it; otherwise, create a new file
        mode = 'a' if file_exists else 'w'
        
        # Create a DataFrame from the scraped data
        df = pd.DataFrame(data, columns=['Text'])

        # Write the DataFrame to the output file
        df.to_csv(output_file, mode=mode, index=False, header=not file_exists)
        
        logging.info("Data scraped successfully and saved to %s", output_file)
        
    except Exception as e:
        logging.error("An error occurred while saving data to CSV: %s", str(e))

def save_to_mysql(data, connection):
    """
    Save scraped data to a MySQL database.
    
    Parameters:
        data (list): The data to be saved.
        connection (mysql.connector.connection.MySQLConnection): The MySQL database connection object.
    """
    try:
        cursor = connection.cursor()

        # Insert data into the table
        for item in data:
            cursor.execute("INSERT INTO scraped_data (text) VALUES (%s)", (item,))
        
        connection.commit()
        cursor.close()
        
        logging.info("Data scraped successfully and saved to MySQL database")
        
    except Exception as e:
        logging.error("An error occurred while saving data to MySQL database: %s", str(e))

def search_wikipedia_pages(topic):
    """
    Search Wikipedia for pages related to the given topic and return their URLs.
    
    Parameters:
        topic (str): The topic to search for on Wikipedia.
    
    Returns:
        list: A list of URLs of Wikipedia pages related to the topic.
    """
    try:
        # Send a GET request to Wikipedia's search endpoint
        search_url = f"https://en.wikipedia.org/w/index.php?search={topic.replace(' ', '+')}"
        response = requests.get(search_url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content of the search results page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract URLs of Wikipedia pages from the search results
        page_urls = []
        for link in soup.find_all('a', href=True):
            href = link.get('href')
            if href.startswith('/wiki/') and not href.endswith('redlink=1'):
                page_urls.append(f"https://en.wikipedia.org{href}")
        
        return page_urls
        
    except requests.exceptions.RequestException as e:
        logging.error("An error occurred while sending the URL request: %s", str(e))
        raise 
    
    except Exception as e:
        logging.error("An error occurred during Wikipedia search: %s", str(e))
        return []

def main():
    parser = argparse.ArgumentParser(description="Scrape data from Wikipedia pages related to a given topic and save it to a CSV file or MySQL database")
    parser.add_argument("--topic", required=True, help="The topic to search for on Wikipedia")
    parser.add_argument("--config", default="config.json", help="The filename of the JSON configuration file")
    parser.add_argument("--mysql_config", default="mysql_config.json", help="The filename of the JSON configuration file for MySQL")
    args = parser.parse_args()

    # Load configuration from file
    config = load_config(args.config)

    # Connect to MySQL database
    connection = connect_to_mysql(args.mysql_config)

    # Search Wikipedia for pages related to the topic
    page_urls = search_wikipedia_pages(args.topic)

    # Scrape data from each Wikipedia page
    for url in page_urls:
        data = scrape_wikipedia_page(url)

        # Save the scraped data to a CSV file or MySQL database based on configuration
        if config['output_format'] == 'csv':
            save_to_csv(data, config['output_file'])
        elif config['output_format'] == 'mysql':
            save_to_mysql(data, connection)
        else:
            logging.error("Invalid output format specified in the configuration file")

    # Close MySQL connection
    connection.close()

if __name__ == "__main__":
    main()
