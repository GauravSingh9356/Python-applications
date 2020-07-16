import time

# Changed the method of opening the browser.
# Selenium allows for the page to be refreshed.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# adding ability to change number of repeats
count = int(input("Number of times to be repeated: "))
# Same as before
#url = input("Enter the URL : ")
print("Length of video:")
minutes = int(input("Minutes "))
seconds = int(input("Seconds "))
PATH = "C:\\Users\\gs935\\Downloads\\Compressed\\chromedriver_win32\\chromedriver.exe"
# Calculating the refreshrate from the user input
refreshrate = minutes * 60 + seconds
# Selecting Safari as the browser

options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
# if url.startswith("https://"):
#     driver.get(url)
# else:
#     driver.get("https://" + url)

driver = webdriver.Chrome(PATH, options=options)
url = 'https://www.youtube.com/watch?v=FW_3b5iPhIE&list=RDFW_3b5iPhIE&index=1'
driver.get(url)
timeout = 5
btn = driver.find_element_by_xpath('//*[@id="movie_player"]/div[5]/button')
btn.click()
for i in range(count):
    # Sets the page to refresh at the refreshrate.
    # element_present = EC.presence_of_element_located(
    #     (By.XPATH, '//*[@id="movie_player"]/div[5]/button'))
    # WebDriverWait(driver, timeout).until(element_present)
    quality = driver.find_element_by_xpath(
        '//*[@id="movie_player"]/div[30]/div[2]/div[3]/button[3]')
    quality.click()

    time.sleep(refreshrate)
    driver.refresh()
