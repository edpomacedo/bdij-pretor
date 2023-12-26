import os
import sys
import hashlib

# Adiciona o diretório pai ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def salvar_arquivo_wikitext(consulta_sparql, tabela_wikitext):
    hash_nome_arquivo = hashlib.md5(consulta_sparql.encode('utf-8')).hexdigest()
    caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'documents', 'wikitext', f'{hash_nome_arquivo}.txt')

    # Criar o diretório se não existir
    os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)

    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(tabela_wikitext)

    return caminho_arquivo
