from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://google.com')
search_q = driver.find_element_by_name("q")
search_q.send_keys("Привет")
search_q.submit() #send_keys(Keys.RETURN) ----> второй вариант
driver.quit()