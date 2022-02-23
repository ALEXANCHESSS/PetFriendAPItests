import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as chrome_options



# driver = webdriver.Chrome(options=options)
# for ChromeDriver version 79.0.3945.16 or over
# options.add_argument("--disable-blink-features=AutomationControlled")

# headless mode
# options.add_argument("--headless")
# options.headless = True
# driver = webdriver.Chrome(options=options)



def test_petfriends(driver):
    driver.find_element_by_css_selector(".btn.btn-success").click()
    driver.find_element_by_xpath("(//a[@href='/login'])").click()  # У меня уже есть аккаунт
    driver.find_element_by_id("email").send_keys('kuznetsov_alex95@mail.ru')  # Ввод емейла
    driver.find_element_by_id('pass').send_keys('1234')  # Ввод пароля
    driver.find_element_by_xpath('(//button[@type="submit"])').click()
    driver.find_element_by_link_text('Мои питомцы').click()
    # if driver.current_url == 'https://petfriends1.herokuapp.com/all_pets':
    #     # Make the screenshot of browser window:
    #     driver.save_screenshot('result_petfriends.png')
    # else:
    #     raise Exception("login error")
    score_pet_fact = len(driver.find_elements_by_tag_name('tr')) - 1
    score_pet_chet = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]").text.split()
    score_pet_chet = int(score_pet_chet[3])
    driver.implicitly_wait(10)
    quantity_photo = len(driver.find_elements_by_css_selector('img[src=""]'))
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/all_pets"]')))
    driver.implicitly_wait(10)
    assert score_pet_fact/2 <= quantity_photo
    assert score_pet_fact == score_pet_chet











