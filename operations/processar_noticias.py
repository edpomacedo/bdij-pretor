# Pretor/1.5.1 - @edpomacedo - operations/processar_noticias.py
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Adicione o diretório raiz do projeto ao caminho do sistema
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import feedparser
from urllib.parse import urlparse  
from utils.feeds_list import feeds
# from gtts import gTTS
from modules.extrair_palavra_chave import extrair_palavra_chave
from modules.tratar_texto_html import limpar_html_para_markdown
from modules.salvar_noticia_markdown import salvar_noticia_como_markdown
from modules.categorizar_noticias_rss import categorizar_noticias_rss

def processar_noticias():
    print("Escolha um feed para processar:")
    for i, feed in enumerate(feeds, 1):
        print(f"{i}. {feed['name']}")

    escolha = int(input("Digite o número do feed desejado: "))

    if 1 <= escolha <= len(feeds):
        feed_url = feeds[escolha - 1]['url']
    else:
        print("Opção inválida. Saindo do programa.")
        return  # Encerrar a função se a escolha for inválida

    pasta_destino = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'documents', 'noticias'))

    # Realizar a coleta de notícias Atom
    feed_atom = feedparser.parse(feed_url)

    # Iterar sobre as entradas do feed Atom
    for i, entry in enumerate(feed_atom.entries):
        titulo = entry.title
        link = entry.link
        pubdate = entry.published
        descricao = entry.title_detail.value

        # Extrair a palavra-chave do texto da notícia
        palavra_chave = extrair_palavra_chave(descricao)

        # Limpar o conteúdo HTML para Markdown
        content = limpar_html_para_markdown(entry.content[0].value) if 'content' in entry else ""

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
        
        # Caminho do arquivo de áudio
        # caminho_audio = os.path.join(subpasta, f'noticia_{i + 1}.mp3')

        # Converter o conteúdo da notícia em áudio usando gTTS
        # tts = gTTS(content, lang='pt-br')
        # tts.save(caminho_audio)

        # Salvar a notícia no formato Markdown
        salvar_noticia_como_markdown(titulo, link, descricao, pubdate, content, caminho_arquivo)

        print(f"Notícia {i + 1} processada e salva em: {caminho_arquivo}")
        # print(f"Áudio da notícia {i + 1} salvo em: {caminho_audio}")

    # Categorizar as notícias
    categorizar_noticias_rss(feed_atom, pasta_destino)

if __name__ == "__main__":
    processar_noticias()
