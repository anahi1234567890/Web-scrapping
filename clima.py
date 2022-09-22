from ctypes.wintypes import HCOLORSPACE
from operator import index
from turtle import pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas

driver = webdriver.Chrome(executable_path=r"D:\User\Anahi\Documents\Escuela\SEMESTRE_7\SQA\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.clima.com/")
driver.find_element(By.XPATH,"//li[@class='m_list_countrys_mx']/a").click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="term"]').send_keys('Querétaro')
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, 'li:nth-child(1) .item-name').click()
time.sleep(3)
driver.find_element(By.XPATH,"//a[contains(text(),\'Por horas\')]").click()
time.sleep(3)

txt_columns= driver.find_element(By.XPATH, '//*[@id="cityTable"]/div[1]/section/ul[1]/li[2]/h2/a')
txt_columns = txt_columns.text

todays_wather = txt_columns.split('Hoy')[0].split('\n')[1:-1]
horas=list()
temp=list()
v_viento=list()

for i in range(0, len(todays_wather),3):
    horas.append(todays_wather[i])
    temp.append(todays_wather[i+1])
    v_viento.append(todays_wather[i+2])

df = pd.DataFrame({'Horas': horas, 'Temperatura': temp, 'Viento km/hr':v_viento})
print(df)
#df.to_cvs('tiempo_hoy.csv', index=False)

driver.quit()