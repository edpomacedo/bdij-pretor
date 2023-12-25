# Pretor/1.5 - @edpomacedo - modules/categorizar_noticias_rss.py
import os
from urllib.parse import urlparse
from modules.extrair_palavra_chave import extrair_palavra_chave
from modules.tratar_texto_html import limpar_html_para_markdown
from modules.salvar_noticia_markdown import salvar_noticia_como_markdown

def categorizar_noticias_rss(feed, pasta_destino):
    # Verificar se a pasta de destino existe, caso contrário, criá-la
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    # Iterar sobre as entradas do feed Atom
    for i, entry in enumerate(feed.entries):
        titulo = entry.title
        link = entry.link
        pubdate = entry.published
        descricao = entry.title_detail.value

        # Limpar o conteúdo HTML para Markdown
        content = limpar_html_para_markdown(entry.content[0].value) if 'content' in entry else ""

        # Extrair a palavra-chave do texto da notícia
        palavra_chave = extrair_palavra_chave(descricao)

        # Criar o caminho da subpasta com base na palavra-chave
        subpasta = os.path.join(pasta_destino, palavra_chave)

        # Verificar se a subpasta existe, caso contrário, criá-la
        if not os.path.exists(subpasta):
            os.makedirs(subpasta)

        # Extrair o identificador único da URL para usar no nome do arquivo
        url_path = urlparse(link).path
        identificador = url_path.strip('/').replace('/', '_')

        # Criar o caminho do arquivo com base no título da notícia
        caminho_arquivo = os.path.join(subpasta, f'noticia_{i + 1}.md')

        # Salvar a notícia no formato Markdown
        salvar_noticia_como_markdown(titulo, link, descricao, pubdate, content, caminho_arquivo)

        print(f"Notícia {i + 1} processada e salva em: {caminho_arquivo}")