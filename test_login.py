from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
def test_1():
  options = webdriver.ChromeOptions()
  options.add_argument("--headless")
  driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
  driver.get("https://demo.opencart.com/admin/")
  op=driver.title
  assert op=="Administration",'mismatched title'

