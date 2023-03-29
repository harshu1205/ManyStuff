import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

Link = "https://one.uf.edu/soc/registration-search/2231?term=%222231%22&category=%22CWSP%22&course-code=%22cop2271%22"
driver.get(Link)
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

# MainLabel = soup.find(class_="sc-jgbSNz sdODo")
# AllSeatLabels = MainLabel.findAll(class_="sc-lbOyJj gCAuOZ")
AllSeatLabels = soup.findAll(class_="sc-lbOyJj gCAuOZ")

LoginContent = driver.page_source
LoginSoup = BeautifulSoup(content, features="html.parser")

if LoginSoup.title.text == "Web Login Service - University of Florida":
    UserElement = driver.find_element(By.ID, "username")
    driver.execute_script("arguments[0].setAttribute('value', 'akulasriharshith')",UserElement);

    PassElement = driver.find_element(By.ID, "password")
    driver.execute_script("arguments[0].setAttribute('value', 'Srihar@125')",PassElement);

    time.sleep(5)

    # LoginSoup.find(id="username").value = "akulasriharshith"
    # LoginSoup.find(id="password").value = "Srihar@125"

    driver.find_element(By.NAME, "_eventId_proceed").click()

time.sleep(50)

LastContent = driver.page_source
LastSoup = BeautifulSoup(LastContent, features="html.parser")
print(len(AllSeatLabels))
print(LastSoup)


# sc-lbOyJj gCAuOZ

# AllSeatLabels = soup.find(class_="sc-lbOyJj gCAuOZ")
#
# requests.post("https://ntfy.sh/cop2271open",
#     data="check yo one.uf boi",
#     headers={
#         "Title": "COP2271ClassOpen",
#     })