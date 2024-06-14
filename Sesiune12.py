import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_JavaScript_Alerts(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()
    def test_JS_Alert(self):
        self.driver.find_element(By.CSS_SELECTOR, "[onclick='jsAlert()']").click()
        self.driver.switch_to.alert.accept()
        time.sleep(3)
        assert self.driver.find_element(By.ID, "result").text == "You successfully clicked an alert"
    def test_JS_Confirm(self):
        self.driver.find_element(By.CSS_SELECTOR, "[onclick='jsConfirm()']").click()
        self.driver.switch_to.alert.accept()
        assert self.driver.find_element(By.ID, "result").text == "You clicked: Ok"
        self.driver.find_element(By.CSS_SELECTOR, "[onclick='jsConfirm()']").click()
        self.driver.switch_to.alert.dismiss()
        assert self.driver.find_element(By.ID, "result").text == "You clicked: Cancel"
    def test_JS_prompt(self):
        self.driver.find_element(By.CSS_SELECTOR, "[onclick='jsPrompt()']").click()
        self.driver.switch_to.alert.send_keys("Test")
        self.driver.switch_to.alert.accept()
        assert self.driver.find_element(By.ID, "result").text == "You entered: Test"
        self.driver.find_element(By.CSS_SELECTOR, "[onclick='jsPrompt()']").click()
        self.driver.switch_to.alert.send_keys("Test")
        self.driver.switch_to.alert.dismiss()
        assert self.driver.find_element(By.ID, "result").text == "You entered: null"

