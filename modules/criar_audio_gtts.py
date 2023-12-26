# Pretor/1.6 - @edpomacedo - modules/criar_audio_gtts.py
import os
from gtts import gTTS

def criar_audio_gTTS():
    # Solicitar ao usuário o subdiretório onde está o arquivo .md
    subdiretorio = input("Digite o subdiretório em documents/noticias onde está o arquivo .md (com / no final): ")

    # Construir o caminho completo para o diretório
    diretorio_noticias = os.path.join("documents", "noticias", subdiretorio)

    # Verificar se o diretório existe
    if os.path.exists(diretorio_noticias):
        # Listar arquivos .md no diretório
        arquivos_md = [f for f in os.listdir(diretorio_noticias) if f.endswith('.md')]

        # Verificar se há arquivos .md
        if not arquivos_md:
            print(f"Nenhum arquivo .md encontrado em {diretorio_noticias}.")
            return

        # Solicitar ao usuário qual arquivo .md deseja transformar em áudio
        print("Arquivos .md disponíveis:")
        for i, arquivo_md in enumerate(arquivos_md):
            print(f"{i + 1}. {arquivo_md}")

        escolha_arquivo = int(input("Digite o número do arquivo .md que deseja transformar em áudio: ")) - 1

        if 0 <= escolha_arquivo < len(arquivos_md):
            # Obter o nome do arquivo .md escolhido
            nome_arquivo_md = arquivos_md[escolha_arquivo]

            # Construir o caminho completo para o arquivo .md escolhido
            arquivo_md_path = os.path.join(diretorio_noticias, nome_arquivo_md)

            # Ler o conteúdo do arquivo .md
            with open(arquivo_md_path, 'r', encoding='utf-8') as arquivo_md:
                texto = arquivo_md.read()

            # Construir o caminho completo para o arquivo de áudio usando o nome do arquivo .md
            nome_arquivo_audio = os.path.splitext(nome_arquivo_md)[0]  # Remover a extensão .md
            audio_path = os.path.join("documents", "audio", f"{nome_arquivo_audio}.mp3")

            # Usar gTTS para converter o texto em áudio
            tts = gTTS(text=texto, lang='pt')
            tts.save(audio_path)

            print(f"Áudio salvo como: {audio_path}")
        else:
            print("Escolha de arquivo inválida.")
    else:
        print(f"O diretório {diretorio_noticias} não foi encontrado.")

# Chamar a função para criar o áudio apenas se o módulo estiver sendo executado diretamente
if __name__ == "__main__":
    criar_audio_gTTS()
