from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException

credenciales = [
    ("cangri@gmail.com","12345funao"),
    ("karol_dance@gmail.com","12346funao"),
    ("locoRene69@gmail.com","12347funao"),
    ("carlitaWASAAAA89._'¿@no_teAcoldai.com","12348funao"),
    ("karol_dance5@funao.com","12349funao"),
    ("karol_dance6@funao.com","12341funao"),
    ("karol_dance7@funao.com","12342funao"),
    ("karol_dance8@funao.com","12343funao"),
    ("karol_dance9@funao.com","12344funao"),
    ("karol_dance20@funao.com","123411funao"),
]

url = "http://localhost/Control/Control/login.php"

options = webdriver.ChromeOptions()
# options.add_argument("--headless=new")
options.add_argument("--window-size=1200,900")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)

try:
    for index, (username, password) in enumerate(credenciales, start=1):
        print(f"[{index}/{len(credenciales)}] Probando credencial: {username} / {password}")

        driver.get(url)

        try:
            # Espera hasta que los campos sean interactuables (un solo elemento)
            uname = wait.until(EC.element_to_be_clickable((By.NAME, "user_name")))
            pwd = wait.until(EC.element_to_be_clickable((By.NAME, "user_password")))
        except TimeoutException:
            print(f"  ❌ No se encontraron los campos en la página para la credencial {username}. Continuando...")
            continue

        try:
            # limpiar y enviar
            uname.clear()
            uname.send_keys(username)

            pwd.clear()
            pwd.send_keys(password)

            # enviar con Enter
            pwd.send_keys(Keys.RETURN)

            sleep(1.2)
        except ElementNotInteractableException:
            print(f"  ❌ Elemento no interactuable para {username}. Continuando...")
            continue

    print("PROCESO TERMINADO")
finally:
    driver.quit()
