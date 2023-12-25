# Pretor/1.5 - @edpomacedo - modules/extrair_palavra_chave.py
from bs4 import BeautifulSoup
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tag import pos_tag

def extrair_palavra_chave(texto):
    # Remover tags HTML usando BeautifulSoup
    soup = BeautifulSoup(texto, 'html.parser')
    texto_limpo = soup.get_text()

    # Tokenização e remoção de stop words
    tokens = word_tokenize(texto_limpo.lower())
    stop_words = set(stopwords.words("portuguese"))
    tokens = [token for token in tokens if token.isalnum() and token not in stop_words]

    # Identificação da frequência das palavras
    frequencia = FreqDist(tokens)

    # Escolha da palavra mais frequente que não seja um determinante (DT) ou preposição (IN)
    palavra_chave = max(frequencia, key=lambda x: frequencia[x] if pos_tag([x])[0][1] not in ['DT', 'IN'] else 0)

    return palavra_chave