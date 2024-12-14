# импортировали пакет Selenium WebDriver
from selenium import webdriver

# создали драйвер
driver = webdriver.Chrome()
driver.maximize_window() # полноэкранный режим
# открыли страницу
driver.get('https://ya.ru/')

current_url = driver.current_url
# assert current_url == 'https://ya.ru/'

assert driver.current_url == 'https://ya.ru/'

driver.quit()