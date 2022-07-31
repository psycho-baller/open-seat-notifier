# %%
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
from selenium import webdriver

import warnings
from bs4 import BeautifulSoup as bs
# import webbrowser

from webdriver_manager.chrome import ChromeDriverManager


options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--headless")
with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# remove the options argument if u wanna see the browser open and perform the automated process
# %%
def get_links(username,password):
    url = 'https://ucalgary.sona-systems.com'
    user_ID = username
    password = password

    driver.get(url)
    driver.find_element(
        By.ID, "ctl00_ContentPlaceHolder1_userid").send_keys(user_ID)
    driver.find_element(By.ID, "pw").send_keys(password)
    element = driver.find_element(
        By.ID, "ctl00_ContentPlaceHolder1_default_auth_button")
    driver.execute_script("arguments[0].click();", element)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.ID, "lnkStudySignupLink"))).click()

    # %%
    html = driver.page_source
    home_page = 'https://ucalgary.sona-systems.com/'
    soup = bs(html, 'html.parser')
    table_row = soup.find('tr').parent.findNextSibling()
    study_links = table_row.findAll('a')

    links = set()
    for link in study_links:
        links.add(f'{home_page}{link.get("href")}')

    return links