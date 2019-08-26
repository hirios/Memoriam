import requests
from bs4 import BeautifulSoup
import os
import subprocess
import socket
import time

busca = input('Nome do filme: ')
busca = busca.split()
termos_da_busca = []

for item in range(len(busca)-1):
    termos_da_busca.append(busca[item] + '+')

concatenando = "".join(termos_da_busca)
# busca[len(busca)-1] Retorna a último palavra capturada pelo input
url = concatenando + busca[len(busca)-1]
url_final = 'https://www.baixarfilmetorrent.net/?s='+url

print()
print("Carregando lista de filmes...")
print()

req = requests.get(url_final)
soup = BeautifulSoup(req.text, 'html.parser')
listagem_da_pesquisa = soup.find_all("div", {'class':  'item'})

titulos = []
links = []

for filme in listagem_da_pesquisa:
    titulos.append(str(filme).split('"')[5])
    links.append(str(filme).split('"')[3])

for titulo in range(0, len(titulos)):
    print([titulo + 1], titulos[titulo])

print()
select_number = int(input('Selecione um número: '))
lin = links[select_number - 1]

link = requests.get(lin)
soup = BeautifulSoup(link.text, 'html.parser')
tabelas = soup.find_all("table")

resolut = []
magnetico = []

for tabela in range(0, len(tabelas)):
    single_table = BeautifulSoup(str(tabelas[tabela]), 'html.parser')
    strong = single_table.find("strong")
    html_qualidades = single_table.find_all("td", {'class':  'td-mv-res'})
    html_magnetic = single_table.find_all("td", {'class':  'td-mv-dow'})

    for quali in range(0, len(html_qualidades)):
        resolut.append(f"{html_qualidades[quali].string} {strong.string}")

    for link_mag in range(len(html_magnetic)):
        magnetico.append(str(html_magnetic[link_mag]).split('"')[3])

for cont in range(0, len(magnetico)):
    print([cont + 1], resolut[cont])

print()
selected_resolution = int(input('Esolha a resolução: '))
mag_final = magnetico[selected_resolution - 1]

print()
print("Aguarde o carregamento... \nEnjoy!!")

start = "peerflix", mag_final
server = " ".join(start)
ip = socket.gethostbyname(socket.gethostname())
subir_server = subprocess.Popen(server, shell=True)
time.sleep(3)
vlc_start = subprocess.Popen(["vlcc.lnk", f"http://{ip}:8888"], shell=True)
