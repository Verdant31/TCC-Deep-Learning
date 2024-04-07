from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
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



time.sleep(9999)
