# Pretor/1.7 - @edpomacedo - modules/sintetizar_texto_audio.py
from google.cloud import texttospeech

def text_to_speech(texto):
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=texto)

    voice = texttospeech.VoiceSelectionParams(
        language_code="pt-BR",
        name="pt-BR-Standard-B",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    return response.audio_content

def salvar_audio(audio_content, output_path):
    with open(output_path, "wb") as out_file:
        out_file.write(audio_content)

    print(f"Áudio salvo como: {output_path}")
