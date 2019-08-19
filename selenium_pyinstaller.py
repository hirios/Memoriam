import sys
import os
import re

options = Options()
options.headless = True

def localizar_driver():
	if getattr(sys, 'frozen', False) :
		chromedriver_path = os.path.join(sys._MEIPASS, 'chromedriver')
		return webdriver.Chrome(chromedriver_path, chrome_options=options)
    
# Para construir: pyinstaller --onefile --add-binary 'chromedriver:.' script.py
