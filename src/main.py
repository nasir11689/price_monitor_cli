import os

from api_client import get_bitcoin_price
from logic import analyze_price

print("Crypto Price Monitor Initialized")
def main():
    # In production, these might come from Environment Variables or a Database
    # MY_TARGET = 60000 
    MY_TARGET = float(os.getenv("TARGET_PRICE", 60000))
    
    print("--- Starting Crypto Monitor ---")
    price = get_bitcoin_price()
    
    if price:
        result = analyze_price(price, MY_TARGET)
        print(result)
    else:
        print("Could not retrieve price. check your connection.")

if __name__ == "__main__":
    main()