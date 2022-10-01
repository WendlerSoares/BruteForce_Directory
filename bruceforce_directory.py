import requests

arquivo = open("listadiretorio.txt")

linhas = arquivo.readlines()

url = "http://site.com.br"

for linha in linhas:
    codigo = 404
    if linha[0] != "#":
        resp = requests.get(url+linha)
        codigo = resp.status_code
    if codigo != 404:
        print(url+linha,codigo)
