from selenium import webdriver
from selenium.webdriver.chrome.options import Options # Importantando opções do chromedriver
import sys
import os

# Atribuindo opção headless ao driver
options = Options()
options.headless = True


def localizar_driver():
	if getattr(sys, 'frozen', False) :
		chromedriver_path = os.path.join(sys._MEIPASS, 'chromedriver')
		return webdriver.Chrome(chromedriver_path, chrome_options=options)
    
# Para construir no linux: pyinstaller --onefile --add-binary 'chromedriver:.' script.py

# Para construir no windows: pyinstaller --onefile --add-binary "chromedriver.exe;." script.py

# pyinstaller --onefile --add-data "node.msi;." script.py


# Comando para iniciar um aplicativo no windows
import sys
import os


def localizar_driver():
	if getattr(sys, 'frozen', False) :
		path = os.path.join(sys._MEIPASS, 'node.msi')
		return path

os.system(f'"{localizar_driver()}"')

subprocess.Popen([f"{path()}vlcc.lnk", comand], shell=True)
os.system(f'"{localizar_driver()}vlcc.lnk"')
