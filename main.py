# Pretor/1.1 - @edpomacedo - main.py
import sys
import os

# Adicionando o diretório principal ao PATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importando as operações
from operations.processar_ementas import processar_ementas
from operations.processar_informativos import processar_informativos

# Seleção de processo a executar via terminal
def main():
    print("Selecione a operação que deseja realizar:")
    print("1. Processar ementas")
    print("2. Processar informativos")

    escolha = input("Digite o número da operação desejada: ")

    if escolha == "1":
        processar_ementas()
    elif escolha == "2":
        processar_informativos()
    else:
        print("Opção inválida. Encerrando o programa.")

if __name__ == "__main__":
    main()
