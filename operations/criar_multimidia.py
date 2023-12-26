# Pretor/1.6 - @edpomacedo - operations/criar_multimedia.py
import sys
import os

# Adiciona o diretório pai ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.extrair_imagem_unsplash import extrair_imagem_unsplash
from modules.criar_audio_gtts import criar_audio_gTTS
from modules.criar_video_clip import criar_video_mp4

def criar_multimidia():
    extrair_imagem_unsplash()
    criar_audio_gTTS()
    criar_video_mp4()

# Exporta a função para ser chamada em outros módulos quando o script for executado diretamente
if __name__ == "__main__":
    criar_multimidia()
