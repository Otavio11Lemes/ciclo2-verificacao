from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

# Inicializa o WebDriver
options = Options()
options.accept_insecure_certs = True
options.add_argument("--proxy-server='direct://'")  # Permite redirecionamento local
options.add_argument("--proxy-bypass-list=*")

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Acessa a página de login local
driver.get("http://127.0.0.1:5000/")

# Usa WebDriverWait para esperar que os elementos estejam presentes
username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "username"))
)
password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "password"))
)

# Preenche o formulário de login
username_input.send_keys("admin")
password_input.send_keys("password")

# Espera até que o botão de login esteja clicável e clique nele
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)
login_button.click()

# Espera um pouco para ver o resultado
time.sleep(3)

# Fecha o driver
driver.quit()
