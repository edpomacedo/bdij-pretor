# Pretor/1.3 - @edpomacedo - modules/analisar_html.py
from bs4 import BeautifulSoup

def analisar_html(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    pre_tag = soup.find('pre')
    return pre_tag.text if pre_tag else None