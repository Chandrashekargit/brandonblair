from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[
    NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])

search = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='twotabsearchtextbox']")))
search.send_keys("iphone xr mobile phone")
time.sleep(2)
search.send_keys(Keys.ENTER)

count = 1
for j in range(1, 12):
    print('Page: ', j)
    d = wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, "//div[@data-index and @data-component-type='s-search-result']")))
    print('items: ', len(d))
    for i in range(1, len(d)):
        iphone_results = wait.until(EC.presence_of_element_located((By.XPATH,
            "//div[@data-index="+str(i)+"]/div/span/div/div//div[2]//div[2]/div[@class='sg-col-inner']"))).text
        print(iphone_results)
        print('count: ', count)
        count += 1
        print('*' * 50)
        if count == len(d):
            pagination = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@class='a-last']")))
            pagination.click()
            print("Next Page Clicked")
            count = 1

# driver.quit()
