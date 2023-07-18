from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
option=webdriver.ChromeOptions()
option.headless=True
driver=webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=option)
driver.get("https://demo.opencart.com/admin/")
# op=driver.title
# assert (op,"Administration")