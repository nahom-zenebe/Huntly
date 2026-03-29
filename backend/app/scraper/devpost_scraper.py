from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from config.settings import URL


def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # run in background
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    return driver



def scrape_devpost():
    driver = init_driver()
    driver.get("https://devpost.com/hackathons")

    time.sleep(5)
    scroll_page(driver)

    hackathons = driver.find_elements(By.CLASS_NAME, "hackathon-tile")

    results = []

    for hack in hackathons:
        try:
            title = hack.find_element(By.TAG_NAME, "h3").text
            link = hack.find_element(By.TAG_NAME, "a").get_attribute("href")

            results.append({
                "title": title,
                "url": link
            })
        except:
            continue

    driver.quit()
    return results

    

def scroll_page(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")

    for _ in range(5):  # scroll 5 times
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height