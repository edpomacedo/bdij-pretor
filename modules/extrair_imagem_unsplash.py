# Pretor/1.6 - @edpomacedo - modules/extrair_imagem_unsplash.py
import sys
import os
import requests

# Adiciona o diretório pai ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importa o módulo config agora que o diretório pai está no sys.path
from config import UNSPLASH_CONFIG

# Chave de API do Unsplash
api_key = UNSPLASH_CONFIG['access_key']

def extrair_imagem_unsplash():
    # Solicitar a query no terminal
    query = input("Digite a query para a busca de imagem no Unsplash: ")

    # URL da API Unsplash
    url = 'https://api.unsplash.com/photos/random'

    # Parâmetros de consulta para especificar a categoria e a quantidade de resultados
    params = {
        'query': query,
        'count': 1,
        'client_id': api_key
    }

    # Faz a solicitação à API
    response = requests.get(url, params=params)

    # Verifica se a solicitação foi bem-sucedida (código de status HTTP 200)
    if response.status_code == 200:
        # Converte a resposta JSON em um dicionário Python
        data = response.json()
    
        # Extrai o URL da imagem
        image_url = data[0]['urls']['regular']
    
        # Baixa a imagem
        image_response = requests.get(image_url)
        
        # Cria o diretório se não existir
        directory = os.path.join(os.path.dirname(__file__), '..', 'documents', 'imagens')
        if not os.path.exists(directory):
            os.makedirs(directory)
    
        # Salva a imagem em um arquivo
        with open(os.path.join(directory, f'{query}.jpg'), 'wb') as image_file:
            image_file.write(image_response.content)
    else:
        print(f'Erro na solicitação: {response.status_code}')
