import requests

def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status() # Check for errors
        data = response.json()
        return data["bitcoin"]["usd"]
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None