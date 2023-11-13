from bs4 import BeautifulSoup as BS
import requests
import pandas as pd
import urllib3

url = "https://www.sec.gov/edgar/search/"

def last_fetch_edgar(count=1):
    params = {
    "r":"el#/q=%22ATM%22%20OR%20%22Open%20Market%20Sales%20AgreementSM%22%20OR%20%22at-the-market%22%20OR%20%22Open%20Market%20Sale%20Agreement%22%20OR%20%22Capital%20On%20Demand%20Sales%20Agreement%22",
    "dateRange":"custom",
    "category":"custom",
    "startdt":"2023-10-13",
    "enddt":"2023-10-16",
    "forms":"424B5%2C8-K%2CF-3%2CF-3ASR%2CS-3%2CS-3ASR"
    }

    headers = {
        # 'User-agent': 'Mozilla/5.0',
        "User-Agent": "Kyle Personal kylev@gmail.com",
        "Accept-Encoding":"gzip, deflate",
        "Host":"www.sec.gov"
    }
    
    response = requests.get(
        url, params=params, headers=headers
    )
    
    soup = BS(response.content, 'html.parser')
    
    hits = soup.find(attrs={'id':'hits'})
    table = hits.find('table')
    tbody = table.find_all('tbody')
    print(tbody)
    
    tr = hits.find_all('tr')
    print(tr)
    
    # tr = tbody.findAll('tr')
    # lista = []
    # for row in tr:
    #     td = row.findAll('td')
    #     lista.append({ 'Team': td[0].text, "Name": td[1].text, "Number": td[2].text, "Minute": td[5].text })



    
    
    return  []
