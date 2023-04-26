from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
import shutil
import time
from selenium.webdriver.common.keys import Keys


driver_path = R"/usr/local/bin/geckodriver"

# path to firefox executable
firefox_path = R"/bin/firefox"

# create options
options = Options()
# options.add_argument('-headless')

# set binary location
options.binary_location = firefox_path

# create a service object and set executable_path to driver_path
service = Service(executable_path=driver_path)

# create a driver
# options.add_argument("~/.config/google-chrome")
driver = webdriver.Firefox(options=options, service=service)

url = "https://www.spreaker.com/show/investors-edge"


driver.get(url)

# driver.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/div[2]/button").click()

time.sleep(3)
try:
    driver.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/div[2]/button").click()
    time.sleep(2)
except:
    pass

for i in range(1,10):
    print(i)                               #/html/body/div[2]/div/div[3]/div/div/div[4]/div/div[1]/div/div/div/div[4]/ul/li[1]/div/div/div[2]/a
    episode = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div/div[4]/div/div[1]/div/div/div/div[4]/ul/li["+str(i)+"]/div/div/div[2]/a")   
    episode.click()
    download = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/a[2]/span")
    download.click()
    time.sleep(1)
    driver.back()
    time.sleep(2)


