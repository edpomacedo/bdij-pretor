# Pretor/1.1 - @edpomacedo - operations/processar_informativos.py
import os
from modules.obter_entrada_usuario import obter_entrada_usuario
from modules.obter_token_edicao import obter_token_edicao
from modules.validar_credenciais import validar_credenciais
from modules.verificar_secao_existe import verificar_secao_existe
from modules.adicionar_secao import adicionar_secao
from modules.realizar_edicao import realizar_edicao

def processar_informativos():
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

            # Usar a primeira linha como título, a segunda como seção, e o restante como corpo da postagem
            page_title = linhas[0].strip()
            section = linhas[1].strip()
            post_content = ''.join(linhas[2:]).strip()

            # Verificar se a seção existe e realizar a edição, ou adicionar a seção e realizar a edição
            if verificar_secao_existe(page_title, section, oauth):
                realizar_edicao(page_title, section, post_content, token, oauth, arquivo)
            else:
                adicionar_secao(page_title, section, post_content, token, oauth, arquivo)

if __name__ == "__main__":
    processar_informativos()
