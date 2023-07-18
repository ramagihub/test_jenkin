from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://demo.opencart.com/admin/")
# op=driver.title
# assert (op,"Administration")