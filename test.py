import requests
from bs4 import BeautifulSoup

def open_first_link(brand):
    """
    Retrieve the first link from a web page and open it in the default web browser.
    
    Parameters:
    url (str): The URL of the web page to open.
    
    Returns:
    None
    """
    url = 'https://www.ethicalconsumer.org/search?keywords='+brand
    ethical = None
    boycotts = None
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
    while not found and line !="":
        #print(line)
        if '<h3 class="search-result__title">' in line:
            found = True
        line = fv.readline()


    index = line.index('"')
    line = line[index+1:]
    index = line.index('"')
    line = line[:index]
    fv.close()
    print('https://www.ethicalconsumer.org/'+line)
    # Send an HTTP GET request to the URL and retrieve the response
    response = requests.get('https://www.ethicalconsumer.org/'+line)
    
    # Use BeautifulSoup to parse the HTML content of the response
    soup = BeautifulSoup(response.text, 'html.parser')

     #open file and write html to it
    fv = open('temp.txt',"w+")
    fv.writelines(soup.prettify())
    fv.close()


    fv = open('temp.txt','r')
    line = fv.readline()
    found = False
    while not found and line!='':
        if '"<b>Ethical Consumer Best Buy:</b>"' in line:
            found = True
        line = fv.readline()
    if found:
        print('in found')
        if 'Yes' in line:
            ethical = True
        else:
            ethical = False


    found = False
    while not found and line!='':
        if '"<b>Boycotts:</b>"' in line:
            found = True
        line = fv.readline()

        if found:
            if 'Yes' in line:
                boycotts = True
            else:
                boycotts = False
    fv.close()

    return ethical,boycotts

        
print(open_first_link('adidas'))



    
    