import requests
import argparse
import logging
from bs4 import BeautifulSoup
import pandas as pd

# Configure logging
logging.basicConfig(filename='scraping.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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
        
    except Exception as e:
        print("An error occurred while scraping the Wikipedia page:", str(e))
        return []

def save_to_csv(data, output_file):
    """
    Save scraped data to a CSV file.
    
    Parameters:
        data (list): The data to be saved.
        output_file (str): The filename for the output CSV file.
    """
    try:
        # Create a DataFrame from the scraped data
        df = pd.DataFrame(data, columns=['Text'])

        # Write the DataFrame to the output file
        df.to_csv(output_file, index=False)
        
        print("Data scraped successfully and saved to", output_file)
        
    except Exception as e:
        print("An error occurred while saving data to CSV:", str(e))

def main():
    parser = argparse.ArgumentParser(description="Scrape data from a Wikipedia page and save it to a CSV file")
    parser.add_argument("url", help="The URL of the Wikipedia page to scrape")
    parser.add_argument("output_file", help="The filename for the output CSV file")
    args = parser.parse_args()

    # Scrape data from the Wikipedia page
    data = scrape_wikipedia_page(args.url)

    # Save the scraped data to a CSV file
    save_to_csv(data, args.output_file)

if __name__ == "__main__":
    main()