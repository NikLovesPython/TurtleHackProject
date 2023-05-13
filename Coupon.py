from googlesearch import search
import requests
from bs4 import BeautifulSoup

def coupon_website_links(brand):
    """
    return array with 3 Links:
    [0] Coupon site
    [1] Comapny site
    [2] Company enviroment impact site
    """

    links = ["","",""]

    search = brand

    if " " in search:
        "".join(search.split(" "))

    CouponSite = "https://www.joinhoney.com/search?q={}".format(search)
    links[0] = CouponSite

    

    CompanySite = search_google(brand)
    links[1] = CompanySite

    ImpactSite =search_google("{} environment impact".format(brand))
    links[2] = ImpactSite

    return links

def search_google(query):
    """
    Search Google for a query and return the URL of the first search result.

    Parameters:
    query (str): The query to search for.

    Returns:
    str: The URL of the first search result, or None if no search results were found.
    """
    search = query
    url = 'https://www.google.com/search'

    headers = {
        'Accept' : '/',
        'Accept-Language': 'en-US,en;q=0.5',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82',
    }
    parameters = {'q': search}

    content = requests.get(url, headers = headers, params = parameters).text
    soup = BeautifulSoup(content, 'html.parser')

    search = soup.find(id = 'search')
    first_link = search.find('a')

    return first_link['href']


coupon_website_links('Nike')
