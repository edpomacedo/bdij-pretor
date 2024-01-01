# Pretor/1.9.1 - @edpomacedo - operations/criar_enunciado.py
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

def criar_enunciado():
    # Pergunta ao usuário sobre a classe de enunciado
    classes_disponiveis = ['Súmula', 'Súmula Vinculante', 'Tema']
    classe_enunciado = obter_selecao_usuario(classes_disponiveis)

    # Mapeamento das QID para lexical_category de acordo com a classe de enunciado
    mapeamento_classe_lexical_category = {
        'Súmula': 'Q2908',
        'Súmula Vinculante': 'Q2907',
        'Tema': 'Q2940'
        # Adicione outras classes conforme necessário
    }

    # Seleção da QID com base na classe de enunciado
    lexical_category = mapeamento_classe_lexical_category.get(classe_enunciado, 'QOUTRA_QID')

    # Pergunta ao usuário sobre a origem do enunciado
    origens_disponiveis = ['STF', 'STJ']
    origem_enunciado = obter_selecao_usuario(origens_disponiveis)

    # Mapeamento das QID para a origem de acordo com a origem do enunciado
    mapeamento_origem_qid = {
        'STF': 'Q1718',
        'STJ': 'Q1721'
        # Adicione outras origens conforme necessário
    }

    # Seleção da QID com base na origem do enunciado
    origem_qid = mapeamento_origem_qid.get(origem_enunciado, 'QOUTRA_QID')

    # Pergunta ao usuário sobre o primeiro_valor e o ultimo_valor
    primeiro_valor = int(input("5) Informe o primeiro_valor: "))
    ultimo_valor = int(input("6) Informe o ultimo_valor: "))

    # Loop para criar lexemas com valores de 'Art. x' a 'Art. y'
    for i in range(primeiro_valor, ultimo_valor + 1):
        # Crie um novo lexema para a categoria lexical fornecida
        lexeme = wbi.lexeme.new(lexical_category=lexical_category)

        # Defina os lemas em português
        lexeme.lemmas.set(language='pt-br', value=f'{classe_enunciado} {i} do {origem_enunciado}')

        # Escreva o lexema
        lexeme.write()

        # Registra os atos em logs e os imprime no terminal
        data_hora_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        mensagem = f'{classe_enunciado} {i} do {origem_enunciado} adicionado com sucesso'
        logger.info(mensagem)
        print(f'[{data_hora_atual}] {mensagem}')

if __name__ == "__main__":
    criar_enunciado()
