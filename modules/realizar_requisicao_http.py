# Pretor/1.3 - @edpomacedo - modules/realizar_requisicao_http.py
import requests

# Realizar requisição http na URL fornecida pelo terminal
def realizar_requisicao_http(url):
    response = requests.get(url)
    return response