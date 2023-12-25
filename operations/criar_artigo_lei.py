# Pretor/1.2 - @edpomacedo - operations/criar_artigo_lei.py
from modules.iniciar_integrator import wbi
from datetime import datetime
from utils.logger import logger

def criar_artigo_lei(primeiro_valor, ultimo_valor, norma_juridica):
    # Loop para criar lexemas com valores de 'Art. x' a 'Art. y'
    for i in range(primeiro_valor, ultimo_valor):
        # Crie um novo lexema para a categoria lexical fornecida
        lexeme = wbi.lexeme.new(lexical_category=norma_juridica)

        # Defina os lemas em português
        lexeme.lemmas.set(language='pt-br', value=f'Art. {i}')

        # Escreva o lexema
        lexeme.write()

        # Registra os atos em logs e os imprime no terminal
        data_hora_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        mensagem = f'Art. {i} da {norma_juridica} adicionado com sucesso'
        logger.info(mensagem)
        print(f'[{data_hora_atual}] {mensagem}')

if __name__ == "__main__":
    criar_artigo_lei()