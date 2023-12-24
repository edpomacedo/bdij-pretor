# Pretor/1.1 - @edpomacedo - modules/verificar_secao_existe.py
import requests
from config import MEDIAWIKI_CONFIG

def verificar_secao_existe(page_title, section, oauth):
    # URL para verificar se a página existe
    api_page_url = MEDIAWIKI_CONFIG['api_url'] + f'?action=query&titles=Talk:{page_title}&format=json'
    response_page = requests.get(url=api_page_url, auth=oauth)

    # Verificar o status da resposta
    if response_page.status_code == 200:
        pages = response_page.json()['query']['pages']
        page_exists = list(pages.keys())[0] != "-1"

        if not page_exists:
            return False

        # URL para verificar se a seção existe
        api_section_url = MEDIAWIKI_CONFIG['api_url'] + f'?action=parse&page={page_title}&prop=sections&format=json'
        response_section = requests.get(url=api_section_url, auth=oauth)

        # Verificar o status da resposta
        if response_section.status_code == 200:
            parsed_data = response_section.json().get('parse', {})
            sections = parsed_data.get('sections', [])
            for entry in sections:
                if entry['line'] == section:
                    return True
            return False
        else:
            raise Exception(f'A chave "error" está presente na resposta JSON. Mensagem de erro: {parsed_data.get("error", {}).get("info", "N/A")}')
    else:
        raise Exception(f'Erro ao verificar se a página existe. Status: {response_page.status_code}, Resposta: {response_page.text}')