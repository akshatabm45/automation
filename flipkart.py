'''from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chr_options = Options()
chr_options.add_experimental_option('detach', True)

serv_object =Service(executable_path=r"C:\browserdrivers\chromedriver.exe")
driver =webdriver.Chrome(service=serv_object, options=chr_options)
driver.get("https://www.flipkart.com/account/login?ret=/")
driver.maximize_window()
driver.find_element(By.CLASS_NAME,"q2U9_I").send_keys("8050586103")
driver.find_element(By.CLASS_NAME,"dSM5Ub Kv3ekh KcXDCU").click()'''



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option("detach", True)

service = Service(r"C:\\browserdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.flipkart.com/account/login?ret=/")
driver.maximize_window()

wait = WebDriverWait(driver, 15)

mobile_input = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//input[@type='text']")
    )
)
mobile_input.send_keys("8050586103")

login_btn = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button//span[text()='Request OTP']")
    )
)
login_btn.click()