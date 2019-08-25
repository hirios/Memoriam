from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
import subprocess
import os
import re

options = Options()
options.headless = True

def localizar_driver():
    if os.path.isfile('chromedriver') or os.path.isfile('chromedriver.exe'):
        if os.name == 'posix':
            # Retorna o driver nos sistas operacionais posix(ubuntu, etc...)
            return webdriver.Chrome(os.getcwd() + '/chromedriver', options=options)
        elif os.name == 'nt':
            # Retorna o driver no sistema operacional windows
            return webdriver.Chrome(executable_path=os.getcwd() + '\chromedriver.exe', chrome_options=options)
        else:
            print('Sistema operacional, não reconhecido.')
            print('Envie o resultado abaixo para os desenvolvedores em https://github.com/hirios/raspamb/')
            print(os.name)
            exit()
    else:
        print('Nao encontrei o driver na mesma pasta do arquivo\nTentarei pela path do sistema')
        return webdriver.Chrome()


def links_zippyshare():
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    global lista_com_links
    lista_com_links = []
    for link in soup.find_all(href=re.compile('zippyshare.com')):
        lista_com_links.append(link['href'])
    return lista_com_links

print('A execução do código pode demorar de acordo com a internet')
print()

url = 'https://www.anbient.com/anime/lista'
html = requests.get(url)
bs = BeautifulSoup(html.text, 'html.parser')
data = bs.find(class_="list")
dat = data.find_all("a")
tv = data.find_all("a", href=True)
# epi = data.find_all("td", {'class':  'epi'})

lista = []
for c in range(0, len(dat)):
    d = dat[c].text
    lista.append(str(d).lower())


def retornar_busca():
    global driver
    global list_animes
    
    quantidade_anime = 0
    list_animes = []
    tv_anbient = []
    while quantidade_anime == 0:
        anime = input('Nome do anime: ').lower().strip()
        print()
        for c in range(0, len(lista)):
            names = lista[c].find(anime)
            if names != (-1):
                list_animes.append(lista[c])
                tv_anbient.append(tv[c].get('href'))
                quantidade_anime = len(list_animes)
        if len(list_animes) == 0:
            print('Certifique-se que o nome está correto!')
            print()

    # Imprime a lista de animes
    for i in range(0, len(list_animes)):
        print(f'[{i + 1}] {list_animes[i].title()}')
    print()

    lista_numero_animes = []
    while True:
        try:
            numero = int(input('Digite um número (-1 para voltar): '))
            print()
            if numero == -1:
                retornar_busca()
            if (numero - 1) < len(list_animes):
                link = 'https://www.anbient.com{}'.format(tv_anbient[numero - 1])
                # print(link)
                break
            else:
                print('Numero invalido!!!\n')
                print()
        except ValueError:
            print('!!!!! USE APENAS NUMEROS !!!!!!')
            print()
        except Exception as e:
            print('Tem outra coisa dando bosta aq')
            print(e)

    print('Capturando links dos episódios...')
    print('Recomenda-se que o chromedriver esteja na mesma pasta que este script')
    print()
    
    try:
        driver = localizar_driver()
        driver.get(link)
    except WebDriverException as e:
        print('Ocorreu um erro')
        print(e)
        exit()

    lista_links = links_zippyshare()
    # Imprime a lista de animes
    for i in range(0, len(lista_links)):
        print(f'[{i + 1}] {lista_links[i]}')

    while True:
        # Le o numero do episódio que ira baixar
        while True:
            try:
                print()
                numero_episodio = int(input('Número do episódio (-1 para voltar): '))
                if numero_episodio == -1:
                    retornar_busca()
                elif numero_episodio <= len(lista_links):
                    link = lista_links[numero_episodio - 1]
                    break
                else:
                    print('Episódio invalido, escolha um numero entre 1 e {}'.format(len(lista_links)))
            except ValueError:
                print('''!!!! Atenção !!!! Erro no número''')

        print()
        print('Carregando anime...')
        print()
        driver.get(link)
        sopa = BeautifulSoup(driver.page_source, 'html.parser')
        zip_link = sopa.find_all("a", id=True)
        zip = zip_link[0].get('href')
        picotado = str(link).split('/')
        comand = f"https://{picotado[2]}{zip}"
        start = subprocess.check_call(["vlc", comand])

retornar_busca()
