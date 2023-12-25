# Pretor/1.2 - @edpomacedo - main.py
import sys
import os

# Adicionando o diretório principal ao PATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importando as operações
from operations.processar_ementas import processar_ementas
from operations.processar_informativos import processar_informativos
from operations.criar_artigo_lei import criar_artigo_lei

# Seleção de processo a executar via terminal
def main():
    print("Selecione a operação que deseja realizar:")
    print("1. Processar ementas")
    print("2. Processar informativos")
    print("3. Criar artigo de legislação")

    escolha = input("Digite o número da operação desejada: ")

    if escolha == "1":
        processar_ementas()
    elif escolha == "2":
        processar_informativos()
    elif escolha == "3":
        # Inquirir valores no terminal
        primeiro_valor = int(input("Digite o primeiro valor numérico para o loop: "))
        ultimo_valor = int(input("Digite o último valor para o loop (exclusive): "))
        norma_juridica = input("Digite o QID da norma jurídica (ex. Q2561): ")

        # Chamar a função com os valores fornecidos
        criar_artigo_lei(primeiro_valor, ultimo_valor, norma_juridica)
    else:
        print("Opção inválida. Encerrando o programa.")

if __name__ == "__main__":
    main()
