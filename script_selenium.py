# EXERCICE 6

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys    
import unittest

class TestSearchEngine(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search(self):        
        driver = self.driver
        driver.get("https://www.google.com")

        # Vérifier que le titre contient "Google"
        self.assertIn("Google", driver.title)

        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("automatisation des tests logiciels")
        search_box.send_keys(Keys.RETURN)

        self.assertIn("automatisation des tests logiciels", driver.page_source)

        results = driver.find_elements(By.CSS_SELECTOR, 'div.yuRUbf a')
        self.assertTrue(any("automatisation des tests logiciels" in result.text for result in results))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
