import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from parameterized import parameterized

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path='D:/Обучение/chromedriver.exe')
FIXTURE_MAIL = [
          ('email1', 'passw1'), ('email2', 'passw2'),
          ('email3', 'passw3'), ('email4', 'passw4')
          ]


class test_homepage(unittest.TestCase):

    @parameterized.expand(FIXTURE_MAIL)
    def test_first_stage_email(self, email: str, passw: str):
        driver.get("https://passport.yandex.ru/auth/")
        time.sleep(2)
        path_to_button_mail = driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]'
            '/div[3]/div/div/div/div[1]/form/div[1]/div[1]/button'
            )
        path_to_button_mail.send_keys(Keys.RETURN)
        time.sleep(2)
        input_email = driver.find_element(By.ID, "passp-field-login")
        input_email.send_keys(email)
        button_login_email = driver.find_element(By.ID, "passp:sign-in")
        button_login_email.send_keys(Keys.RETURN)
        time.sleep(2)
        input_passw = driver.find_element(By.ID, "passp-field-passwd")
        input_passw.send_keys(passw)
        button_enter_passw = driver.find_element(By.ID, "passp:sign-in")
        button_enter_passw.send_keys(Keys.RETURN)
        time.sleep(3)
        self.assertEqual(driver.current_url, "https://passport.yandex.ru/profile")
        driver.close()


    def test_second_stage_phone(self, phone: int, code: int):
        driver.get("https://passport.yandex.ru/auth/")
        time.sleep(2)
        path_to_button_phone = driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div'
            '/div[2]/div[3]/div/div/div/div[1]/form/div[1]/div[2]/button'
            )
        path_to_button_phone.send_keys(Keys.RETURN)
        time.sleep(2)
        input_phone = driver.find_element(By.ID, "passp-field-login")
        input_phone.send_keys(phone)
        button_login_phone = driver.find_element(By.ID, "passp:sign-in")
        button_login_phone.send_keys(Keys.RETURN)
        time.sleep(2)
        input_passw = driver.find_element(By.ID, "passp-field-phoneCode")
        input_passw.send_keys(code)
        button_enter_passw = driver.find_element(
            By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div/'
            'div[2]/div[3]/div/div/form/div/div[3]/button[1]'
            )
        button_enter_passw.send_keys(Keys.RETURN)
        time.sleep(2)
        self.assertEqual(driver.current_url, "https://passport.yandex.ru/profile")
        driver.close()
