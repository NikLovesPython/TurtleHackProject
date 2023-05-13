'''import requests
from bs4 import BeautifulSoup

# Enter the brand for which you want to find coupons
brand = input("Enter a brand name: ")

# Define the URL of the coupon website you want to scrape
url = f"https://www.coupons.com/coupon-codes/{brand}/"

# Send a GET request to the website
response = requests.get(url)

# Use BeautifulSoup to parse the HTML content of the website
soup = BeautifulSoup(response.content, "html.parser")

# Find all the coupon codes on the website
coupon_codes = soup.find_all("div", class_="Code--codeText--3lLse")

# Print the coupon codes
print(f"Here are the coupon codes for {brand}:")
for code in coupon_codes:
    print(code.text)'''
    
import requests
from bs4 import BeautifulSoup

def open_first_link(url):
    """
    Retrieve the first link from a web page and open it in the default web browser.
    
    Parameters:
    url (str): The URL of the web page to open.
    
    Returns:
    None
    """
    # Send an HTTP GET request to the URL and retrieve the response
    response = requests.get(url)
    
    # Use BeautifulSoup to parse the HTML content of the response
    soup = BeautifulSoup(response.text, 'html.parser')
    
    #open file and write html to ir
    fv = open('temp.txt',"w+")
    fv.writelines(soup.prettify())
    fv.close()
    fv = open('temp.txt',"r")

    line = fv.readline()
    found = False
    print(line)
    while not found and line !="":
        #print(line)
        if '<h3 class="search-result__title">' in line:
            found = True
            print("found string")
        line = fv.readline()

    print(line)

    index = line.index('"')
    line = line[index+1:]
    index = line.index('"')
    line = line[:index]
    fv.close()
    print(line)


    
    
open_first_link('https://www.ethicalconsumer.org/search?keywords=adidas')