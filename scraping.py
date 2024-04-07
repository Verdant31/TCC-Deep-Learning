from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--allow-running-insecure-content')
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
chrome_options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://conteudos.xpi.com.br/acoes/bbas3/grafico/")

chart = driver.find_element(By.ID, "grafico-atv")
scroll_origin = ScrollOrigin.from_viewport(10, 10)
ActionChains(driver).scroll_from_origin(scroll_origin, 0, 500).perform()

iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)

button = driver.find_element(By.CSS_SELECTOR, '[data-tooltip="Estilo da Barra"]')
driver.execute_script("arguments[0].click();", button)
time.sleep(3)

el = driver.find_element(By.CSS_SELECTOR, '[data-value="stepline"]')
el.click()  

driver.save_screenshot("test.png")