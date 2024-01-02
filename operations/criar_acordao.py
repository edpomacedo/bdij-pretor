# Pretor/2.0 - @edpomacedo - operations/criar_acordao.py
from modules.iniciar_integrator import wbi
from datetime import datetime
from utils.logger import logger

def obter_selecao_usuario(opcoes):
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i}) {opcao}")

    while True:
        try:
            escolha = int(input("Selecione uma opção pelo número: "))
            if 1 <= escolha <= len(opcoes):
                return opcoes[escolha - 1]
            else:
                print("Opção inválida. Por favor, escolha um número válido.")
        except ValueError:
            print("Opção inválida. Por favor, escolha um número válido.")

def criar_acordao():
    # Pergunta ao usuário sobre a classe de enunciado
    classes_disponiveis = ['ADPF', 'ADI']
    classe_acordao = obter_selecao_usuario(classes_disponiveis)

    # Mapeamento das QID para lexical_category de acordo com a classe de enunciado
    mapeamento_classe_lexical_category = {
        'ADPF': 'Q2566',
        'ADI': 'Q2565'
        # Adicione outras classes conforme necessário
    }

    # Seleção da QID com base na classe de enunciado
    lexical_category = mapeamento_classe_lexical_category.get(classe_acordao, 'QOUTRA_QID')

    # Pergunta ao usuário sobre a origem do enunciado
    origens_disponiveis = ['STF']
    origem_enunciado = obter_selecao_usuario(origens_disponiveis)

    # Mapeamento das QID para a origem de acordo com a origem do enunciado
    mapeamento_origem_qid = {
        'STF': 'Q1718'
        # Adicione outras origens conforme necessário
    }

    # Seleção da QID com base na origem do enunciado
    origem_qid = mapeamento_origem_qid.get(origem_enunciado, 'QOUTRA_QID')

    # Pergunta ao usuário sobre o primeiro_valor e o ultimo_valor
    primeiro_valor = int(input("5) Informe o primeiro valor: "))
    ultimo_valor = int(input("6) Informe o ultimo valor: "))

    # Loop para criar lexemas com valores de 'ENUNCIADO N do ORIGEM' a 'ENUNCIADO Y do ORIGEM'
    for i in range(primeiro_valor, ultimo_valor + 1):
        # Crie um novo lexema para a categoria lexical fornecida
        lexeme = wbi.lexeme.new(lexical_category=lexical_category)

        # Defina os lemas em português
        lexeme.lemmas.set(language='pt-br', value=f'{classe_acordao} {i}')

        # Escreva o lexema
        lexeme.write()

        # Registra os atos em logs e os imprime no terminal
        data_hora_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        mensagem = f'{classe_acordao} {i} do {origem_enunciado} adicionado com sucesso'
        logger.info(mensagem)
        print(f'[{data_hora_atual}] {mensagem}')

if __name__ == "__main__":
    criar_acordao()
