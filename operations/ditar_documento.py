import os
from modules.sintetizar_texto_audio import text_to_speech, salvar_audio

def obter_lista_documentos(diretorio):
    documentos = [f for f in os.listdir(diretorio) if f.endswith('.txt')]
    return documentos

def mostrar_e_selecionar_documento(documentos):
    print("Documentos disponíveis:")
    for i, documento in enumerate(documentos):
        print(f"{i + 1}. {documento}")

    escolha = input("Digite o número do documento que deseja processar: ")
    return escolha

def ditar_documento():
    # Diretório dos documentos de texto
    diretorio_base = 'documents'
    diretorio_documentos = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', diretorio_base, 'legendas')

    # Imprimir o caminho absoluto para fins de depuração
    print(f"Caminho absoluto do diretório 'legendas': {os.path.abspath(diretorio_documentos)}")

    # Verificar se o diretório existe
    if not os.path.exists(diretorio_documentos):
        print(f'O diretório {diretorio_documentos} não foi encontrado.')
        return

    # Obter a lista de documentos no diretório
    documentos = obter_lista_documentos(diretorio_documentos)

    # Verificar se há documentos disponíveis
    if not documentos:
        print(f'Nenhum documento encontrado em {diretorio_documentos}.')
        return

    # Exibir documentos e permitir que o usuário escolha
    escolha_documento = mostrar_e_selecionar_documento(documentos)

    # Verificar se a escolha é válida
    try:
        escolha_documento = int(escolha_documento)
        if 1 <= escolha_documento <= len(documentos):
            # Obter o caminho completo do arquivo escolhido
            input_file_path = os.path.join(diretorio_documentos, documentos[escolha_documento - 1])
        else:
            print("Escolha inválida.")
            return
    except ValueError:
        print("Escolha inválida.")
        return

    # Ler o conteúdo do arquivo de texto
    with open(input_file_path, 'r', encoding='utf-8') as arquivo_texto:
        texto = arquivo_texto.read()

    # Chamar a função para sintetizar o texto em áudio
    audio_content = text_to_speech(texto)

    # Diretório para salvar o áudio
    output_directory = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), diretorio_base, 'audio')

    # Criar o diretório se não existir
    os.makedirs(output_directory, exist_ok=True)

    # Construir o caminho completo para o arquivo de áudio
    output_file_path = os.path.join(output_directory, f"{os.path.splitext(documentos[escolha_documento - 1])[0]}.wav")

    # Chamar a função para salvar o áudio
    salvar_audio(audio_content, output_file_path)

if __name__ == '__main__':
    ditar_documento()
