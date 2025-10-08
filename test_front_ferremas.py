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

url = "http://localhost/Control_testing/login.php"

options = webdriver.ChromeOptions()
# options.add_argument("--headless=new")  # si lo tienes activado NO verás la ventana
options.add_argument("--window-size=1200,900")
# Esta opción evita que Chrome se cierre cuando el script termina
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)

try:
    for index, (username, password) in enumerate(credenciales, start=1):
        print(f"[{index}/{len(credenciales)}] Probando: {username} / {password}")
        driver.get(url)

        try:
            uname = wait.until(EC.element_to_be_clickable((By.NAME, "user_name")))
            pwd = wait.until(EC.element_to_be_clickable((By.NAME, "user_password")))
        except TimeoutException:
            print(f"  ❌ No se encontraron los campos para {username}. Saltando...")
            continue  # avanza a la siguiente credencial

        uname.clear()
        uname.send_keys(username)
        pwd.clear()
        pwd.send_keys(password)
        pwd.send_keys(Keys.RETURN)

        sleep(1.2)

    # ejemplo: intentar login admin al final (si quieres)
    admin_user = "admin"
    admin_password = "admin"
    try:
        # volver a la página por si acaso
        driver.get(url)
        uname = wait.until(EC.element_to_be_clickable((By.NAME, "user_name")))
        pwd = wait.until(EC.element_to_be_clickable((By.NAME, "user_password")))

        uname.clear()
        uname.send_keys(admin_user)
        pwd.clear()
        pwd.send_keys(admin_password)
        pwd.send_keys(Keys.RETURN)

        prduc = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "img-responsive")))

        prduc.click()
        print("Intento admin realizado.")
    except TimeoutException:
        print("  ❌ No se pudo realizar login admin: campos no encontrados.")

    print("PROCESO TERMINADO (la ventana de Chrome se mantendrá abierta gracias a 'detach').")
    input("Presiona Enter para cerrar el navegador y terminar el script...")

except Exception as e:
    print("Ocurrió un error inesperado:", e)
finally:
    # Si quieres que se cierre automáticamente al finalizar, descomenta la siguiente línea:
    # driver.quit()
    pass