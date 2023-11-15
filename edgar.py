from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common import exceptions

class Crawler:
    def __init__(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

        url = "https://www.sec.gov/edgar/search/?r=el#/q=%2522ATM%2522%2520OR%2520%2522Open%2520Market%2520Sales%2520AgreementSM%2522%2520OR%2520%2522at-the-market%2522%2520OR%2520%2522Open%2520Market%2520Sale%2520Agreement%2522%2520OR%2520%2522Capital%2520On%2520Demand%2520Sales%2520Agreement%2522&dateRange=custom&category=custom&startdt=2023-10-13&enddt=2023-10-16&forms=424B5%252C8-K%252CF-3%252CF-3ASR%252CS-3%252CS-3ASR"
        self.browser.get(url)

    def fetch_hits(self):
        css_selector_tbody = "#hits"
        hits = self.browser.find_element(By.CSS_SELECTOR, css_selector_tbody)
        table = hits.find_element(By.TAG_NAME, 'table')
        tbody = table.find_element(By.TAG_NAME, 'tbody')
        trs = tbody.find_elements(By.TAG_NAME, 'tr')

        filings = [
        ]

        for tr in trs :
            filetype = tr.find_element(By.CLASS_NAME, 'filetype')
            preview_file = filetype.find_element(By.CLASS_NAME, 'preview-file')
            filename = preview_file.text
            filed_date = tr.find_element(By.CLASS_NAME, 'filed').text            
            entity_name = tr.find_element(By.CLASS_NAME, 'entity-name').text

            filings.append(
                {
                    "filename": filename,
                    "entity_name": entity_name,
                    "date": filed_date
                }
            )
                
        return filings

    def reset(self):
        self.browser.refresh()



if __name__ == "__main__":
    from memory import FilingsMemory

    memory = FilingsMemory()
    crawler = Crawler()

    while True:
        filings = crawler.fetch_hits()
        for filing in filings :
            if not memory.exists(filing):
                print("new filing found: ", filing)
                memory.insert(filing)

        if len(filings) == 0:
            print("we have been banned. Sleeping 15 seconds.")
            sleep(15)
            
        crawler.reset()
        
        sleep(5)