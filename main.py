# Pretor/1.8.2 - @edpomacedo - main.py
import os
from operations.processar_ementas import processar_ementas
from operations.processar_informativos import processar_informativos
from operations.criar_artigo_lei import criar_artigo_lei
from operations.criar_lista_entidades import criar_lista_entidades
from operations.extrair_texto_acordao import extrair_texto_acordao
from operations.processar_noticias import processar_noticias
from operations.criar_multimidia import criar_multimidia
from operations.ditar_documento import ditar_documento
from operations.inserir_dispositivo_legal import inserir_dispositivo_legal

def main():
    print("Selecione a operação que deseja realizar:")
    print("1. Processar ementas")
    print("2. Processar informativos")
    print("3. Criar artigo de legislação")
    print("4. Criar lista de entidades")
    print("5. Extrair texto de acórdão")
    print("6. Processar notícias")
    print("7. Criar multimídia")
    print("8. Ditar documento")
    print("9. Inserir dispositivo legal")

    escolha = input("Digite o número da operação desejada: ")

    operacoes = {
        "1": processar_ementas,
        "2": processar_informativos,
        "3": lambda: criar_artigo_lei(int(input("Digite o primeiro valor numérico para o loop: ")),
                                     int(input("Digite o último valor para o loop (exclusive): ")),
                                     input("Digite o QID da norma jurídica (ex. Q2561): ")),
        "4": criar_lista_entidades,
        "5": extrair_texto_acordao,
        "6": processar_noticias,
        "7": criar_multimidia,
        "8": ditar_documento,
        "9": lambda: inserir_dispositivo_legal(),
    }

    if escolha in operacoes:
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        operacoes[escolha]()
    else:
        print("Opção inválida. Encerrando o programa.")

if __name__ == "__main__":
    main()
