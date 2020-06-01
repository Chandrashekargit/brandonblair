import time
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def cwe():
    driver = webdriver.Chrome('/home/junaid/PycharmProjects/HelloWorld/venv/bin/chromedriver_linux64/chromedriver')
    driver.get("https://vulncat.fortify.com/en/weakness")
    driver.maximize_window()
    time.sleep(1)
    wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException])
    click = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='impliedsubmit']")))
    click.click()
    for j in range(1, 135):
        print('page: ', j)
        driver.get("https://vulncat.fortify.com/en/weakness?po="+str(j)+"")
        header = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@data-id]/div[2]")))
        for i in range(1, len(header)+1):
            try:
                id = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-id]["+str(i)+"]")))
                ids = id.get_attribute('data-id')
                print('data_id: ', ids)
                header_text = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@data-id="+str(ids)+"]/div[2]//a"))).text
                header_text1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@data-id="+str(ids)+"]/div[2]//a")))
                print(header_text)
                header_text1.click()
                cwe_value1 = wait.until(EC.element_to_be_clickable((By.XPATH,
                    "//div[@data-id="+str(ids)+"]/div[3]/div[2]/div//div[4]//div[@class='item' and contains(text(),' Standards Mapping - Common Weakness Enumeration ')]"))).text
                print(cwe_value1)
                print("*" * 50)
            except:
                print('NO CWE ID')
                print('*' * 50)
                pass


cwe()
