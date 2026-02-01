def analyze_price(current_price, target_price):
    if current_price <= target_price:
        return f"🚀 BUY ALERT: Price is ${current_price}. Below your target of ${target_price}!"
    else:
        return f"😴 Hold: Price is ${current_price}. Target is ${target_price}."