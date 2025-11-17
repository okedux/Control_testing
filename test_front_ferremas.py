from gevent import monkey
monkey.patch_all()

from time import sleep,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
import locust
import os
import pyautogui

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
capetaCampturas = r"C:\xampp\htdocs\Control_testing\capturas"

options = webdriver.ChromeOptions()
# options.add_argument("--headless=new")  # si lo tienes activado NO verás la ventana
options.add_argument("--window-size=1200,900")
# Esta opción evita que Chrome se cierre cuando el script termina
options.add_experimental_option("detach", True)

try:
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
except Exception as e:
    print("Failed to start Chrome WebDriver. This usually means Chrome is not installed, the ChromeDriver is incompatible, or the driver failed to start.")
    print("Original error:", e)
    raise
wait = WebDriverWait(driver, 10)

def sacar_captura():
    nombre_archivo = os.path.join(capetaCampturas, f"captura_{int(time())}.png")
    imagen = pyautogui.screenshot()
    imagen.save(nombre_archivo)

def loginTest ():
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
    except:
        print('error de login')
    sacar_captura()

def seleccionarProducto():
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

        print("inicio de sesion como admin con exito")

        prduc = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "img-responsive")))

        prduc.click()
        
        agregar_Stock()

        print("prueba de producto realizada con exito")
    except TimeoutException:
        print("  ❌ No se pudo realizar login admin: campos no encontrados.")

    sacar_captura()

def tetsLogout():

    try:

        logout = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"glyphicon-tags")))

        logout.click()

        print('logout completado')
    except TimeoutException:
        print('error al cerrar sesion')
    sacar_captura()

def testeCategoria():
    admin_user = "admin"
    admin_password = "admin"
    try:

        driver.get(url)
        uname = wait.until(EC.element_to_be_clickable((By.NAME, "user_name")))
        pwd = wait.until(EC.element_to_be_clickable((By.NAME, "user_password")))

        uname.clear()
        uname.send_keys(admin_user)
        pwd.clear()
        pwd.send_keys(admin_password)
        pwd.send_keys(Keys.RETURN)

        sleep(2)
            
        categorias = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"glyphicon-tags")))

        categorias.click()

        print('test categoria completo')
        

    except TimeoutException:

        input("no se puedo probar categoria")
    sacar_captura()
def añadir_categoria():
    try:
        añadir = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"pull-right")))
        

        añadir.click()

        sleep(2)

        nom = wait.until(EC.element_to_be_clickable((By.ID, "nombre")))
        des = wait.until(EC.element_to_be_clickable((By.ID, "descripcion")))

        nom.send_keys("wasaaaaa")
        des.send_keys("wasaaaaa de wasaaaaaaa")

        enter = wait.until(EC.element_to_be_clickable((By.ID,"guardar_datos")))

        enter.click()

        close = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"close")))

        close.click()

        print('categoria añadida sin problemas')
    except:
        print('error fatal')
    sacar_captura()

def añadir_usuario():
    try:
        nom="benjamin"
        ape="ojeda"
        use="okedux"
        mail="be.ojedao@duocuc.cl"
        con="GatoWeon69"
        recon="GatoWeon69"


        usuarioSelect = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"glyphicon-user")))

        usuarioSelect.click()

        añadir = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"pull-right")))

        añadir.click()

        print("seleccionar añadir usuario con exito")

        nombre = wait.until(EC.element_to_be_clickable((By.ID,"firstname")))
        apellidos = wait.until(EC.element_to_be_clickable((By.ID,"lastname")))
        usuario= wait.until(EC.element_to_be_clickable((By.ID,"user_name")))
        email = wait.until(EC.element_to_be_clickable((By.ID,"user_email")))
        contraseña = wait.until(EC.element_to_be_clickable((By.ID,"user_password_new")))
        reContraseña = wait.until(EC.element_to_be_clickable((By.ID,"user_password_repeat")))

        nombre.send_keys(nom)
        apellidos.send_keys(ape)
        usuario.send_keys(use)
        email.send_keys(mail)
        contraseña.send_keys(con)
        reContraseña.send_keys(recon)

        reContraseña.send_keys(Keys.RETURN)

        clos = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"close")))

        clos.click()

        print("usuario añadido con exito ")

        logout = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"glyphicon-off")))

        logout.click()

        uname = wait.until(EC.element_to_be_clickable((By.NAME, "user_name")))
        pwd = wait.until(EC.element_to_be_clickable((By.NAME, "user_password")))

        uname.clear()
        uname.send_keys(use)
        pwd.clear()
        pwd.send_keys(con)
        pwd.send_keys(Keys.RETURN)

        print("usuario añadido inicia sesion sin problemas")


    except:
        print("error")
    sacar_captura()

def estres_test():
    class UserBehavior(locust.TaskSet):
        @locust.task
        def login(self):
            self.client.post("/login.php", {
                "user_name": "admin",
                "user_password": "admin"
            })

        @locust.task
        def seleccionar_producto(self):
            self.client.get("/producto.php?id=1")

        @locust.task
        def logout(self):
            self.client.get("/logout.php")

    class WebsiteUser(locust.HttpUser):
        tasks = [UserBehavior]
        wait_time = locust.between(1, 3)
    print('prueba de estres completa')

def agregar_Stock():
    try:
        añadir = driver.find_element(By.XPATH, "//img[contains(@src, 'stock-in.png')]")
        añadir.find_element(By.XPATH, "./parent::a").click()

        cantidad = wait.until(EC.element_to_be_clickable((By.NAME,"quantity")))

        cantidad.clear()
        cantidad.send_keys("19")

        referencia= wait.until(EC.element_to_be_clickable((By.NAME,"reference")))

        referencia.clear()
        referencia.send_keys("wasaaaa")
        referencia.send_keys(Keys.RETURN)

        print("stock agregado con exito")
    except:
        print('no se pudo agregar stock de producto')
    sacar_captura()

def fase1():
    loginTest()
    sacar_captura()
    sleep(5)
    seleccionarProducto()
    sacar_captura()
    sleep(5)
    tetsLogout()
    sacar_captura()
    print("face 1 completa")

def fase2():
    sleep(5)
    testeCategoria()
    sacar_captura()
    sleep(5)
    añadir_categoria()
    sacar_captura()
    sleep(5)
    añadir_usuario()
    sacar_captura()
    sleep(5)
    estres_test()
    sacar_captura()
    print('pruebas realizadas con exito')

try:
    #fase1()
    fase2()

except Exception as e:
    print("Ocurrió un error inesperado:", e)
finally:
    
    pass

