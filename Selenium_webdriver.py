from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

chr_options = Options()
chr_options.add_experimental_option('detach', True)

serv_object =Service(executable_path=r"C:\browserdrivers\chromedriver.exe")
driver =webdriver.Chrome(service=serv_object, options=chr_options)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.find_element(By.CLASS_NAME,"a-button-text").click()

wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.visibility_of_element_located((By.ID, "twotabsearchtextbox")))

search_box.clear()
search_box.send_keys("Redmi")



#element = driver.find_element(By.NAME,"twotabsearchtextbox").send_keys("Redmi")
driver.find_element(By.ID,"nav-search-submit-button").click()
driver.find_element(By.LINK_TEXT,"Redmi A4 5G (Starry Black, 4GB RAM, 128GB Storage) | Segment Largest 6.88in 120Hz | 50MP Dual Camera | 18W Fast Charging | Charger in The Box").click()

windows = driver.window_handles
driver.switch_to.window(windows[1])
#driver.execute_script("window.scrollBy(0, 500);")

wait.until(EC.presence_of_element_located((By.ID, "productTitle")))

# Locate Add to Cart
add_to_cart = wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-button")))

# Scroll into view
driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart)

# Click using JS
driver.execute_script("arguments[0].click();", add_to_cart)
# click Add to Cart
try:
    # Case 1: Added to cart confirmation
    wait.until(EC.visibility_of_element_located((By.ID, "sw-gtc")))
    driver.find_element(By.ID, "sw-gtc").click()
    print("✅ Product added and cart opened")

except:
    print("⚠️ Go to Cart not shown, opening cart manually")

    # Open cart directly
    driver.find_element(By.ID, "nav-cart").click()






