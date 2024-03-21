import requests
from bs4 import BeautifulSoup
import pandas as pd

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

if __name__ == "__main__":
    # URL of the Wikipedia page to scrape
    wikipedia_url = 'https://en.wikipedia.org/wiki/Artificial_intelligence'

    # Output file for storing the scraped data
    output_file = 'wikipedia_ai_data.csv'
    
    # Scrape data from the Wikipedia page
    scraped_data = scrape_wikipedia_page(wikipedia_url)
    
    # Save scraped data to a CSV file
    save_to_csv(scraped_data, output_file)
