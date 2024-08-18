from selenium import webdriver
from selenium.webdriver.common.by import By

class infow():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_info(self, query):
        self.query = query
        self.driver.get("https://www.wikipedia.org")
        search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        search.submit()

# assit = infow()
# assit.get_info("neutron stars")

# input("Press Enter to close the browser window...")
# assit.driver.quit()