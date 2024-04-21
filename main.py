from google.cloud import speech
import os
import io

# Inicializa el cliente de la API de Speech-to-Text
client = speech.SpeechClient()

# Directorio que contiene tus archivos de audio
audio_files_directory = '/home/tu directorio'
audio_files = [f for f in os.listdir(audio_files_directory) if f.startswith('output') and f.endswith('_mono.wav')]

# Configuración para la transcripción
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    language_code="es-ES"
)

# Preparar el archivo para guardar las transcripciones finales
transcription_file_path = os.path.join(audio_files_directory, "transcripcion_final.txt")

# Asegurarse de que el archivo de transcripciones esté vacío al inicio
with open(transcription_file_path, "w") as file:
    file.write("")

# Procesar cada archivo de audio y agregar la transcripción al archivo de texto
for audio_file in sorted(audio_files):
    file_path = os.path.join(audio_files_directory, audio_file)
    with io.open(file_path, "rb") as audio_file:
        content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)

    print(f"Transcribiendo {audio_file.name}...")
    response = client.recognize(config=config, audio=audio)

    # Escribir la transcripción de cada archivo en el archivo de texto
    with open(transcription_file_path, "a") as file:
        for result in response.results:
            transcription = result.alternatives[0].transcript
            file.write(transcription + "\n")

print(f"Transcripción completada. Resultados guardados en: {transcription_file_path}")
