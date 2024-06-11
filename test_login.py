from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def test_1():
  chrome_options = Options()
  chrome_options.add_argument("--headless")  # Run Chrome in headless mode
  chrome_options.add_argument("--disable-gpu")  # Applicable to Windows to avoid error messages
  chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
  chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problem
  options.add_argument("--headless")
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
  driver.get("https://demo.opencart.com/admin/")
  op=driver.title
  assert op=="Administration",'mismatched title'

