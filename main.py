import requests
import time
import uuid

# Function to send the request
def send_request(available_taps, count, token):
    url = 'https://api-gw.geagle.online/tap'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {token}',
        'content-type': 'application/json',
        'origin': 'https://telegram.geagle.online',
        'priority': 'u=1, i',
        'referer': 'https://telegram.geagle.online/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }
    
    timestamp = int(time.time())
    salt = str(uuid.uuid4())
    
    data = {
        "available_taps": available_taps,
        "count": count,
        "timestamp": timestamp,
        "salt": salt
    }
    
    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Read the Bearer tokens from data.txt
with open('data.txt', 'r') as file:
    tokens = [line.strip() for line in file.readlines()]

# Fixed values
available_taps = 1000
count = 300

# Loop to send requests for each token, and repeat the process after completing all accounts
while True:
    for token in tokens:
        response = send_request(available_taps, count, token)
        print(f"Response for token {token}: {response}")
    
    # Wait for 5 minutes before repeating the process for all accounts
    print("Waiting for 5 minutes before repeating...")
    time.sleep(5 * 60)  # Wait for 5 minutes before starting the next iteration
