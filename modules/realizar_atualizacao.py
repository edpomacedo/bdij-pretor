# Pretor/1.3 - @edpomacedo - modules/realizar_atualizacao.py
from datetime import datetime
from config import MEDIAWIKI_CONFIG
import requests
from utils.logger import logger

def realizar_atualizacao(page_title, post_content, token, oauth, nome_arquivo):
    
    # URL para a API de edição do MediaWiki
    api_edit_url = MEDIAWIKI_CONFIG['api_url']

    # Parâmetros para a edição da página, incluindo o token de edição
    params = {
        'action': 'edit',
        'title': page_title,
        'text': post_content,
        'contentformat': 'text/x-wiki',
        'contentmodel': 'wikitext',
        'minor': 'true',
        'recreate': 'true',
        'summary': '',
        'format': 'json',
        'token': token  # Incluir o token de edição
    }

    # Requisição para editar a página
    response = requests.post(url=api_edit_url, auth=oauth, data=params)

    # Verificar o status da resposta
    if response.status_code == 200:
        data_hora_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        mensagem = f'Postagem realizada com sucesso para a página: {page_title}'
        print(f'[{data_hora_atual}] ({nome_arquivo}) {mensagem}')
        logger.info(f'({nome_arquivo}) {mensagem}')
    else:
        data_hora_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        mensagem = f'Erro ao postar para a página {page_title}. Status: {response.status_code}, Resposta: {response.text}'
        print(f'[{data_hora_atual}] ({nome_arquivo}) {mensagem}')
        logger.error(f'({nome_arquivo}) {mensagem}')