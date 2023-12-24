# Pretor/1.1 - @edpomacedo - modules/adicionar_secao.py
from datetime import datetime
import requests
from config import MEDIAWIKI_CONFIG
from utils.logger import logger

def adicionar_secao(page_title, section, post_content, token, oauth, nome_arquivo):
    # URL para a API do MediaWiki para adicionar uma seção
    api_edit_url = MEDIAWIKI_CONFIG['api_url']

    # Parâmetros para adicionar a seção
    params = {
        'action': 'edit',
        'title': f'Talk:{page_title}',
        'section': 'new',  # Criar uma nova seção
        'text': f'== {section} ==\n{post_content}\n',  # Título da nova seção e conteúdo
        'contentformat': 'text/x-wiki',
        'contentmodel': 'wikitext',
        'minor': 'true',
        'summary': '',
        'format': 'json',
        'token': token  # Incluir o token de edição
    }

    # Requisição para adicionar a seção
    response = requests.post(url=api_edit_url, auth=oauth, data=params)

    # Verificar o status da resposta
    if response.status_code == 200:
        data_hora_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        mensagem = f'Seção adicionada com sucesso para a página: {page_title}, seção: {section}'
        logger.info(mensagem)
        print(f'[{data_hora_atual}] {mensagem}')

    else:
        data_hora_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        mensagem = f'Erro ao adicionar a seção {section} para a página {page_title}. Status: {response.status_code}, Resposta: {response.text}'
        logger.error(mensagem)
        print(f'[{data_hora_atual}] {mensagem}')