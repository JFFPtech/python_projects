import requests
import pandas as pd
import logging

def fetch_data(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Failed to fetch data: {e}")
        return None

def save_data_to_csv(data, filename='data.csv'):
    try:
        df = pd.json_normalize(data)
        df.to_csv(filename, index=False)
        logging.info(f"Data saved to {filename}")
    except Exception as e:
        logging.error(f"Failed to save data to CSV: {e}")

if __name__ == "__main__":
    url = 'https://example.com'
    headers = {
        "sec-ch-ua": '"Not A;Brand";v="99", "Chromium";v="121", "Google Chrome";v="121"',
        'referer': 'https://example.com',
        'sec-ch-ua-mobile': '?0',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "sec-ch-ua-platform": "Windows",
    }

    logging.basicConfig(level=logging.INFO)

    data = fetch_data(url, headers)
    if data:
        save_data_to_csv(data)
    else:
        print('Error: Failed to fetch data')
