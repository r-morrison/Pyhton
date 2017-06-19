import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PgaTourCrawl(unittest.tescase):
    def setup:
        self.driver = webdriver.Firefox()

def test_find_player(player):
    driver = self.driver
    driver.get("http://www.pgatour.com")
    assert "Pgatour" in driver.title
    players = driver.find_element_by_xpath("//*[@id='module-1497453290607-786325-6']/div[1]/div/div/div/div[10]/div[1]/ul/li[4]/a/span")
    players.click()
    driver.close()
    
def tearDown(self):
    self.driver.close()