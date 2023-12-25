# Pretor/1.3 - @edpomacedo - modules/enviar_requisicao_sparql.py
import requests

def enviar_requisicao_sparql(consulta_sparql, endpoint_url):
    parametros = {"query": consulta_sparql, "format": "json"}
    response_sparql = requests.post(endpoint_url, data=parametros)
    return response_sparql