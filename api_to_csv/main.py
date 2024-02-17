import requests
import pandas

url = 'https://example.com'

headers = {
    "sec-ch-ua": '"Not A;Brand";v="99", "Chromium";v="121", "Google Chrome";v="121"',
    'referer': 'https://example.com',
    'sec-ch-ua-mobile': '?0',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "sec-ch-ua-platform": "Windows",
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()

    jsonData = response
    data = pandas.json_normalize(jsonData)['data']

    data.to_csv('data.csv', index=False)
else:
    print('Error: failed to get data', response.status_code)