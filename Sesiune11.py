import time
import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestElefant(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.elefant.ro')

    def tearDown(self):
        self.driver.quit()

    def test_search_product(self):
        time.sleep(3)
        self.driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()
        self.driver.find_element(By.XPATH, "//input[@name='SearchTerm']").send_keys('Iphone14')
        self.driver.find_element(By.CSS_SELECTOR, "button[title='Începe căutarea']").click()
        time.sleep(3)
        assert len(self.driver.find_elements(By.CLASS_NAME, 'product-title')) == 2

    def test_search_product_with_waits(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(
                (By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')))
        self.driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()
        self.driver.find_element(By.XPATH, "//input[@name='SearchTerm']").send_keys('Iphone14')
        self.driver.find_element(By.XPATH, "//input[@name='SearchTerm']").send_keys(Keys.BACK_SPACE)
        self.driver.find_element(By.XPATH, "//input[@name='SearchTerm']").send_keys(Keys.ENTER)
        #self.driver.find_element(By.CSS_SELECTOR, "button[title='Începe căutarea']").click()
        self.driver.implicitly_wait(3)
        assert len(self.driver.find_elements(By.CLASS_NAME, 'product-title')) == 2
