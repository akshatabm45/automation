import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#to keep the browser open after script ends
chr_options = Options()
chr_options.add_experimental_option('detach', True)

#passing browser driver executable path
serv_object =Service(executable_path=r'C:\browserdrivers\chromedriver.exe')
driver = webdriver.Chrome(service=serv_object,options=chr_options)

driver.get("https://www.ironspider.ca/forms/checkradio.htm")
driver.maximize_window()
#selecting specific checkbox
#driver.find_element(By.XPATH,"//input[@type='checkbox' and @value='orange']" ).click()

#selecting all the checkboxes
my_elements = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
'''for ele in my_elements:
    ele.click()'''


# selecting multiple checkbox based on choice
'''for ele in my_elements:
    value= ele.get_attribute("value")
    if (value=='yellow') or(value=='green') or(value=='red'):
        ele.click()'''

#selecting last 2 checkbox
for i in range(len(my_elements)-2, len(my_elements)):#4,6
    my_elements[i].click()

#selecting first 2 checkboxes
for i in range(len(my_elements)):
    if i<2:
        my_elements[i].click()

time.sleep(5)
#uncheck al checkboxes
for i in my_elements:
    if i.is_selected():
        i.click()



