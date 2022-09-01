from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(executable_path=r"D:\User\Anahi\Documents\Escuela\SEMESTRE_7\SQA\chromedriver.exe")
driver.get("https://www.clima.com/")
driver.find_element(By.XPATH,"//li[@class='m_list_countrys_mx']/a").click()

driver.find_element(By.XPATH,"//div[@class='m_list_block_cities']/ul/li[21]/a").click()
driver.find_element(By.XPATH,"//a[contains(text(),'Por horas')]").click()

time.sleep(3)