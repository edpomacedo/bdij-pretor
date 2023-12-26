# Pretor/1.6 - @edpomacedo - modules/criar_video_clip.py
import sys
import os
import hashlib
import time

# Adiciona o diretório pai ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from moviepy.editor import AudioFileClip, ImageClip, clips_array

def criar_video_mp4():
    # Solicite ao usuário o nome do arquivo de áudio
    audio_filename = input("Digite o nome do arquivo de áudio (sem o caminho, apenas o nome do arquivo): ")
    audio_path = os.path.join("documents", "audio", audio_filename)
    audio_clip = AudioFileClip(audio_path)

    # Solicite ao usuário o nome do arquivo de imagem
    image_filename = input("Digite o nome do arquivo de imagem (sem o caminho, apenas o nome do arquivo): ")
    image_path = os.path.join("documents", "imagens", image_filename)
    image_clip = ImageClip(image_path, duration=audio_clip.duration)

    # Solicite ao usuário a taxa de quadros desejada para o vídeo
    fps_input = input("Digite a taxa de quadros desejada para o vídeo (padrão: 30 fps): ")
    
    # Defina a taxa de quadros padrão como 30 fps, mas permita que o usuário a modifique
    fps = float(fps_input) if fps_input else 30.0

    # Combine áudio e imagem
    video_clip = clips_array([[image_clip]])
    video_clip = video_clip.set_audio(audio_clip)
    video_clip = video_clip.set_fps(fps)  # Defina a taxa de quadros

    # Gere um nome aleatório para o vídeo usando um hash do timestamp
    video_hash = hashlib.md5(str(time.time()).encode()).hexdigest()
    output_path = os.path.join("documents", "videos", f"{video_hash}.mp4")

    # Salve o resultado
    video_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

    print(f"Vídeo salvo como: {output_path}")

# Chame a função para criar o áudio apenas se o módulo estiver sendo executado diretamente
if __name__ == "__main__":
    criar_video_mp4()
