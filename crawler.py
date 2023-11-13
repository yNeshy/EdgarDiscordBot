from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common import exceptions

browser = webdriver.Firefox()
browser.implicitly_wait(3)


url = "https://www.sec.gov/edgar/search/?r=el#/q=%2522ATM%2522%2520OR%2520%2522Open%2520Market%2520Sales%2520AgreementSM%2522%2520OR%2520%2522at-the-market%2522%2520OR%2520%2522Open%2520Market%2520Sale%2520Agreement%2522%2520OR%2520%2522Capital%2520On%2520Demand%2520Sales%2520Agreement%2522&dateRange=custom&category=custom&startdt=2023-10-13&enddt=2023-10-16&forms=424B5%252C8-K%252CF-3%252CF-3ASR%252CS-3%252CS-3ASR"
browser.get(url)

css_selector_tbody = "#hits"
hits = browser.find_element(By.CSS_SELECTOR, css_selector_tbody)
table = hits.find_element(By.TAG_NAME, 'table')
tbody = table.find_element(By.TAG_NAME, 'tbody')
trs = tbody.find_elements(By.TAG_NAME, 'tr')

for tr in trs :
    print(
        tr.text
)
print("show appart visites lmissa")
filings = [
    
]

for tr in trs :
    filetype = tr.find_element(By.CLASS_NAME, 'filetype')
    preview_file = filetype.find_element(By.CLASS_NAME, 'preview-file')
    filename = preview_file.text

    filed _date = tr.find_element(By.CLASS_NAME, 'filed').text

    # tr.find_element(By.CLASS_NAME, 'enddate')
    
    entity_name = tr.find_element(By.CLASS_NAME, 'entity-name').text
    
    # tr.find_element(By.CLASS_NAME, 'cik')
    # tr.find_element(By.CLASS_NAME, 'biz-location')
    # tr.find_element(By.CLASS_NAME, 'incorporated')
    # tr.find_elements(By.CLASS_NAME, 'file-num')

    filings.append(
        {
            "filename": filename,
            "entity_name": entity_name,
            "date": filed_date
        }
    )

    
