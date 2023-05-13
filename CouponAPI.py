import requests
import json

# Set up the API endpoint URL
url = 'https://api.couponapi.com/search'

# Set up the API parameters
api_key = '<your api key>'  # Replace with your CouponAPI key
brand = 'Nike'  # Replace with the brand you want to search for
params = {
    'api_key': api_key,
    'brand': brand,
}

# Send the API request and retrieve the response
response = requests.get(url, params=params)
coupons = json.loads(response.text)

# Print the coupons
for coupon in coupons['coupons']:
    print(coupon['code'], coupon['description'], coupon['expires_at'])