# Pretor/1.8 - @edpomacedo - operations/inserir_dispositivo_legal.py
import sys
import os

# Adiciona o diretório pai ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from wikibaseintegrator.models import Sense
from modules.iniciar_integrator import wbi

def obter_entity_id():
    return input("Digite o entity_id do lexema (ex. L8299): ")

def obter_subdiretorio_arquivo():
    # Diretório base
    diretorio_base = 'documents/legislacao'

    # Listar subdiretórios
    subdiretorios = [d for d in os.listdir(diretorio_base) if os.path.isdir(os.path.join(diretorio_base, d))]

    # Exibir subdiretórios disponíveis e permitir que o usuário escolha
    print("Subdiretórios disponíveis:")
    for i, subdiretorio in enumerate(subdiretorios):
        print(f"{i + 1}. {subdiretorio}")

    escolha_subdiretorio = input("Digite o número do subdiretório desejado: ")

    # Verificar se a escolha é válida
    try:
        escolha_subdiretorio = int(escolha_subdiretorio)
        if 1 <= escolha_subdiretorio <= len(subdiretorios):
            subdiretorio_escolhido = subdiretorios[escolha_subdiretorio - 1]
        else:
            print("Escolha inválida.")
            return None, None
    except ValueError:
        print("Escolha inválida.")
        return None, None

    # Listar arquivos no subdiretório escolhido
    diretorio_completo = os.path.join(diretorio_base, subdiretorio_escolhido)
    arquivos = [f for f in os.listdir(diretorio_completo) if f.endswith('.txt')]

    # Exibir arquivos disponíveis e permitir que o usuário escolha
    print("Arquivos disponíveis:")
    for i, arquivo in enumerate(arquivos):
        print(f"{i + 1}. {arquivo}")

    escolha_arquivo = input("Digite o número do arquivo desejado: ")

    # Verificar se a escolha é válida
    try:
        escolha_arquivo = int(escolha_arquivo)
        if 1 <= escolha_arquivo <= len(arquivos):
            arquivo_escolhido = arquivos[escolha_arquivo - 1]
        else:
            print("Escolha inválida.")
            return None, None
    except ValueError:
        print("Escolha inválida.")
        return None, None

    return diretorio_completo, arquivo_escolhido

def inserir_dispositivo_legal():
    # Obter o entity_id do lexema
    entity_id = obter_entity_id()

    # Obter o subdiretório e o arquivo de texto
    subdiretorio, arquivo = obter_subdiretorio_arquivo()

    if entity_id and subdiretorio and arquivo:
        # Ler as linhas do arquivo de texto e criar um sentido para cada linha
        with open(os.path.join(subdiretorio, arquivo), 'r', encoding='utf-8') as arquivo_texto:
            for linha in arquivo_texto:
                # Obter o lexema
                lexeme = wbi.lexeme.get(entity_id=entity_id)

                # Criar o sentido
                sense = Sense()
                sense.glosses.set(language='pt-br', value=linha.strip())  # Remover espaços em branco extras

                # Adicionar o sentido ao lexema
                lexeme.senses.add(sense)

                # Escrever o lexema de volta no Wikibase
                lexeme.write()

if __name__ == "__main__":
    inserir_dispositivo_legal()