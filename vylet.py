from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import selenium.common.exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

# чтобы браузер не открывался и работал в фоне
options = Options()
options.add_argument("--headless")


driver_path = r"msedgedriver.exe"
non_list = ["Москва (Шереметьево)","Москва (Домодедово)","Москва (Внуково)","Калининград (Храброво)","Калуга","С.-Петербург (Пулково)",
        "Казань","Ноябрьск","Пермь (Большое Савино)","Череповец","Нижний Новгород"]
night = ["20","21","22","23","00","01","02","03","04","05","06","07","08","09","10"]
day = ["20","19","18","17","16","15","14","13","12","11","10"]
service = Service(driver_path)
driver = webdriver.Edge(service=service,options=options)
driver.get("https://airport.by/raspisanie-rejsov/vylety")
block = driver.find_elements(By.XPATH, "//tbody")
print(block)

pril_1 = driver.find_elements(By.XPATH, '//tr[@class="flights-item flights-item--special yellow"]')
pril_2 = driver.find_elements(By.XPATH, '//tr[@class="flights-item flights-item--special"]')

text_arive_nigrt = 'Ночные вылеты:\n'
text_arive_day = 'Дневные вылеты:\n'
for i in pril_1:
    where = i.find_element(By.XPATH,'.//td[@class="airport_name"]')
    where = where.text
    time = i.find_element(By.XPATH, './/td[@class="flight_time"]')
    time = time.text
    status  = i.find_element(By.XPATH, './/td[@class="flight_status"]')

    if status.text == "Вылетел":
        pass
    elif status.text == "В полёте" and where not in non_list and  time[0:2] in night:
        text_arive_nigrt += f'{where} {time}:\n'
    elif status.text == "В полёте" and where not in non_list and time[0:2] in day:
        text_arive_day+=f'{where} {time}:\n'

for i in pril_2:
    where = i.find_element(By.XPATH,'.//td[@class="airport_name"]')
    where = where.text
    time = i.find_element(By.XPATH, './/td[@class="flight_time"]')
    time = time.text
    status = i.find_element(By.XPATH, './/td[@class="flight_status"]')

    if status.text == "Вылетел":
        pass
    elif where not in non_list and time[0:2] in night:
        text_arive_nigrt+=f'{where} {time}\n'
    elif where not in non_list and time[0:2] in day:
        text_arive_day+=f'{where} {time}\n'

print(text_arive_nigrt)
print(text_arive_day)




#element = driver.find_element_by_id("submit")
#element.click()

#как найти элемент?

#<input type="text" name="passwd" id="passwd-id" />
#element = driver.find_element_by_id("passwd-id")
#element = driver.find_element_by_name("passwd")
#element = driver.find_element_by_xpath("//input[@id='passwd-id']")
#element = driver.find_element_by_xpath("//div[@class="asdasd",text()='текст внутри строчки']")
""" ВСЕ КРОМЕ ID ВЕРНЕТ СПИСОК
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
"""

#ввод
#element.send_keys("some text")
#element.sendKeys(Keys.ENTER)
#driver.findElement(By.id("Value")).sendKeys(Keys.ENTER)

#клик
#element = driver.find_element_by_id("submit")
#element.click()

#вперед назад
#driver.forward()
#driver.back()

#найти значение
#element.get_attribute("value")
#взять текст
#text = driver.find_element_by_class_name("class").getText("my text")

#окна
#driver.switch_to_window("windowName")
#alert = driver.switch_to_alert()


#https://habr.com/ru/post/248559/













