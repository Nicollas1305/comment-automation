from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

chromedriver_path = "/Users/nicollasmarinho/Downloads/chromedriver-mac-x64/chromedriver"
chrome_profile_path = "/Users/nicollasmarinho/Biblioteca/Application Support/Google/Chrome/Default"

options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={chrome_profile_path}")

service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

# Em caso de primeiro login, preencher credenciais
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)


username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")
username_input.send_keys("USERNAME")
password_input.send_keys("SENHA")
password_input.send_keys(Keys.RETURN)
time.sleep(30)
#######

post_url = "https://www.instagram.com/p/URL-DO-POST/"
driver.get(post_url)
time.sleep(5)

with open('followers.json', 'r') as file:
    seguidores = json.load(file)

usernames = [
    follower['string_list_data'][0]['value']
    for follower in seguidores
]

for username in usernames:
    print("Procurando o campo de comentário...")
    try:
        comment_input = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea"))
        )
        comment_input.click()
        comment_input.send_keys(f"@{username}")

        publish_button = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and text()='Publicar']"))
        )
        publish_button.click()

        print(f"Comentário feito: @{username}")
    except Exception as e:
        print(f"Erro ao comentar para @{username}: {e}")
    time.sleep(30)

driver.quit()
