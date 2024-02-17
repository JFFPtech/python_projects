import requests
from bs4 import BeautifulSoup
import pandas as pd
from apscheduler.schedulers.blocking import BlockingScheduler

# URL of the website to scrape
URL = 'https://example.com'

# Output file for storing the scraped data
output_file = 'scraped_data.csv'

# Schedule interval for scraping data (e.g., 'hourly', 'daily', etc.)
schedule_interval = 'daily'

def scrape_data():
    try:
        # Send a GET request to the URL
        response = requests.get(URL)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract data from the website (example)
        data = []
        # Example: Extract all <a> tags and store their text content in the data list
        for link in soup.find_all('a'):
            data.append(link.get_text())

        # Create a DataFrame from the scraped data
        df = pd.DataFrame(data, columns=['Data'])

        # Write the DataFrame to the output file
        df.to_csv(output_file, index=False)
        
        print("Data scraped successfully and saved to", output_file)
        
    except Exception as e:
        print("An error occurred:", str(e))

# Schedule the scraping job
scheduler = BlockingScheduler()
scheduler.add_job(scrape_data, schedule_interval)
print("Scraping job scheduled to run", schedule_interval)
scheduler.start()

# Note:This code includes the following components:

# URL: The URL of the website to scrape. Replace 'https://example.com/' with the actual URL of the target website.

#  Output File: The filename or path for storing the scraped data. Update 'scraped_data.csv' with your desired filename and format (e.g., CSV, JSON).

#   Schedule Interval: The interval at which the scraping job should run (e.g., 'hourly', 'daily'). Adjust schedule_interval variable as needed.

#    Scrape Data Function: The scrape_data() function contains the logic for sending a GET request to the URL, parsing the HTML content using BeautifulSoup, extracting relevant data, and storing it in a DataFrame. 
#    This example extracts text content from all <a> tags on the website.

#    Scheduling: The scraping job is scheduled using the BlockingScheduler from the APScheduler library. The scrape_data() function is called at the specified interval.

#    To run this script, you'll need to install the required libraries (requests, beautifulsoup4, pandas, apscheduler) using pip:

#    pip install requests beautifulsoup4 pandas apscheduler

#    Once installed, you can execute the script, and it will automatically scrape data from the specified website at the scheduled interval and store it in the output file.