# Pretor/1.3 - @edpomacedo - operations/criar_lista_entidades.py
import hashlib

# Adicione o diretório raiz do projeto ao sys.path para testes
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import WIKIBASE_CONFIG

from modules.realizar_requisicao_http import realizar_requisicao_http
from modules.analisar_html import analisar_html
from modules.enviar_requisicao_sparql import enviar_requisicao_sparql
from modules.tratar_resultados import tratar_resultados
from modules.criar_tabela_wikitext import criar_tabela_wikitext
from modules.salvar_arquivo_wikitext import salvar_arquivo_wikitext
from modules.obter_token_edicao import obter_token_edicao
from modules.validar_credenciais import validar_credenciais
from modules.realizar_atualizacao import realizar_atualizacao

def criar_lista_entidades():
    # Solicitar a URL da fonte no terminal
    url_fonte = input("Digite a URL da fonte: ")

    # Realizar a requisição HTTP utilizando o módulo
    response = realizar_requisicao_http(url_fonte)

    # Verificação do status da resposta
    if response.status_code == 200:
        # Obtenção dos resultados
        consulta_sparql = analisar_html(response.text)
    
        if consulta_sparql:
            # Envio da requisição SPARQL utilizando o módulo
            response_sparql = enviar_requisicao_sparql(consulta_sparql, WIKIBASE_CONFIG['url']['endpoint_url'])

            # Verificação do status da resposta
            if response_sparql.status_code == 200:
                # Obtenção dos resultados
                resultados = response_sparql.json()

                # Transforma os resultados em uma lista de dicionários
                dados_tabela = []
                for resultado in resultados["results"]["bindings"]:
                    linha = {chave: valor['value'] for chave, valor in resultado.items()}
                    dados_tabela.append(linha)

                # Validar credenciais
                oauth = validar_credenciais()

                # Obter token de edição
                token_edicao = obter_token_edicao(oauth)
            
                # Perguntar ao usuário o tipo de resultado
                print("Selecione o tipo de resultado:")
                print("1. Lexeme")
                print("2. Item")
                print("3. Property")

                # Obter a resposta do usuário
                opcao = input("Digite o número correspondente à opção desejada: ")

                # Verificar a opção escolhida e realizar tratamento específico
                if opcao in ["1", "2", "3"]:
                    tipo_resultado = ["Lexeme", "Item", "Property"][int(opcao) - 1]
                    dados_tabela = tratar_resultados(dados_tabela, tipo_resultado)

                    # Adiciona os cabeçalhos e contagem de resultados
                    cabeçalhos = dados_tabela[0].keys()
                    contagem_resultados = len(dados_tabela)

                    # Criar tabela wikitext utilizando o novo módulo
                    tabela_wikitext = criar_tabela_wikitext(dados_tabela, cabeçalhos, contagem_resultados)

                    # Salvar o resultado no arquivo utilizando o novo módulo
                    caminho_arquivo = salvar_arquivo_wikitext(url_fonte, tabela_wikitext)
                    print(f"Resultado salvo em: {caminho_arquivo}")

                    # Solicitar o nome da página de destino no terminal
                    nome_pagina_destino = input("Digite o nome da página de destino (com prefixo, se houver): ")

                    # Calcular o hash do caminho do arquivo
                    hash_nome_arquivo = hashlib.md5(caminho_arquivo.encode('utf-8')).hexdigest()

                    # Chamar a função realizar_atualizacao
                    realizar_atualizacao(nome_pagina_destino, tabela_wikitext, token_edicao, oauth, hash_nome_arquivo)

                else:
                    print("Opção inválida. Saindo do programa.")
                    exit()

            else:
                print(f"Falha na requisição SPARQL. Código de status: {response_sparql.status_code}")

        else:
            print("Tag <pre> não encontrada na página.")
    else:
        print(f'Erro na requisição HTTP. Código de status: {response.status_code}')
        exit()

if __name__ == "__main__":
    criar_lista_entidades()