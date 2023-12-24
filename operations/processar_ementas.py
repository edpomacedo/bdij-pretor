# Pretor/1.1 - @edpomacedo - operations/processar_ementas.py
import os
from modules.obter_entrada_usuario import obter_entrada_usuario
from modules.obter_token_edicao import obter_token_edicao
from modules.validar_credenciais import validar_credenciais
from modules.realizar_edicao import realizar_edicao

def processar_ementas():
    # Obtém o caminho para a pasta "documents" do projeto
    diretorio_base = os.path.join(os.getcwd(), 'documents')

    # Solicitar ao usuário o nome do subdiretório onde os arquivos .txt estão localizados
    subdiretorio = obter_entrada_usuario('Informe o subdiretório onde os arquivos .txt estão localizados: ')

    # Monta o caminho completo para o diretório
    diretorio = os.path.join(diretorio_base, subdiretorio)

    # Utilizar as credenciais
    oauth = validar_credenciais()

    # Obter o token de edição
    token = obter_token_edicao(oauth)

    # Iterar sobre os arquivos no diretório
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith(".txt"):
            caminho_arquivo = os.path.join(diretorio, arquivo)

            # Ler o conteúdo do arquivo
            with open(caminho_arquivo, 'r', encoding='utf-8') as file:
                linhas = file.readlines()

            # Usar a primeira linha como título e o restante como corpo da postagem
            page_title = linhas[0].strip()
            post_content = ''.join(linhas[1:])

            # Realizar a verificação e edição na página, passando o nome do arquivo
            realizar_edicao(page_title, post_content, token, oauth, arquivo)

if __name__ == "__main__":
    processar_ementas()
