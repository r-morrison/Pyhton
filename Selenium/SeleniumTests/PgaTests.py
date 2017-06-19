import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PgaTourCrawl(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        

    def test_verify_page(self):
        driver = self.driver
        driver.get("http://www.pgatour.com")
        driver.maximize_window()
        print("Page title: " + driver.title)
        assert "PGATOUR" in driver.title
        
        links = ['LEADERBOARD', 'SCHEDULE', 'PLAYERS', 'FEDEXCUP'
                 ,'VIDEO', 'NEWS', 'STATS', 'FANTASY', 'TICKETS', 'SHOP']
        
        for link in links:
            output = driver.find_element_by_link_text(link)
            print('Link found: ' + output.text)
            self.assertEqual(link, output.text)
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()