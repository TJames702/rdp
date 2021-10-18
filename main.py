# Haithem { Me codes }

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# Haithem { Me Codes }
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://google.com/')
print('Devloped by Haithem ^ Me Codes')

# Haithem { Me codes }
