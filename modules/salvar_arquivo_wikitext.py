# Pretor/1.3 - @edpomacedo - modules/salvar_arquivo_wikitext.py
import os
import hashlib

def salvar_arquivo_wikitext(consulta_sparql, tabela_wikitext):
    hash_nome_arquivo = hashlib.md5(consulta_sparql.encode('utf-8')).hexdigest()
    caminho_arquivo = os.path.join('documents', 'wikitext', f'{hash_nome_arquivo}.txt')

    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(tabela_wikitext)

    return caminho_arquivo