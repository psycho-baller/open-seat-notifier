# %%
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options  # for suppressing the browser
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver

import warnings
from bs4 import BeautifulSoup as bs
# import webbrowser

Options = Options()
Options.add_argument("--headless")
with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    driver = webdriver.Firefox(
        executable_path=GeckoDriverManager().install())
# remove the options argument if u wanna see the browser open and perform the automated process
# %%


def get_links(username, password):
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

def get_details(url):
    driver.get(url)
    html = driver.page_source
    soup = bs(html, 'html.parser')
    title = soup.find('span', {'id': 'ctl00_ContentPlaceHolder1_lblStudyName'}).get_text()
    description = soup.find('span', {'id': 'ctl00_ContentPlaceHolder1_lblLongDesc'}).get_text()
    credits_ = soup.find('span', {'id': 'ctl00_ContentPlaceHolder1_lblCreditTotal'}).get_text()
    duration = soup.find('span', {'id': 'ctl00_ContentPlaceHolder1_lblDuration'}).get_text()
    location = soup.find('div', {'class': 'col-md-11'}).find("strong").get_text().strip("\n\t")
    print(title, description, credits_, duration, location)
    return title, description, credits_, duration, location

def close_driver():
    driver.quit()