# Pretor/1.5 - @edpomacedo - modules/tratar_text_html.py
from bs4 import BeautifulSoup

def limpar_html_para_markdown(texto_html):
    # Remover tags HTML usando BeautifulSoup
    soup = BeautifulSoup(texto_html, 'html.parser')
    texto_limpo = soup.get_text()
    return texto_limpo