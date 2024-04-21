#!/bin/bash

# Directorio donde están tus archivos de audio
DIR="/home/tu directorio"

# Recorrer todos los archivos .wav en el directorio
for file in $DIR/*.wav; do
  echo "Convirtiendo $file a mono..."
  # Construye el nombre del archivo de salida reemplazando .wav con _mono.wav
  outfile=$(echo $file | sed 's/.wav/_mono.wav/')
  
  # Comando para convertir el archivo a mono
  ffmpeg -i "$file" -ac 1 "$outfile"
done

echo "Conversión completada."
