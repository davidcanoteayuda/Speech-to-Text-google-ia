# Video to Text Converter on Orange Pi Zero 3

Video Tutorial
Mira el video completo de este proceso en mi canal de YouTube para una guía visual paso a paso: Video to Text on Orange Pi Zero 3 Tutorial https://youtu.be/c10aOqmXr2M

Este proyecto te guía a través del proceso de configuración de una Orange Pi Zero 3 para convertir el audio de un video a texto utilizando la API de Google Cloud Speech-to-Text.

## Descripción

El repositorio contiene todos los scripts y archivos necesarios para ejecutar la aplicación de conversión de audio de video a texto en una Orange Pi Zero 3. Este proyecto es ideal para aquellos que buscan experimentar con procesamiento de lenguaje natural y reconocimiento de voz en hardware económico.

## Requisitos Previos

- Orange Pi Zero 3 con al menos 1GB de RAM.
- Tarjeta SD con Armbian instalado. [Descargar imagen](https://www.armbian.com/orange-pi-zero-3/)
- Acceso a Internet en la Orange Pi.

## Configuración del Sistema

1. Actualiza el sistema:

   sudo apt update
   sudo apt upgrade
2. Instala Python 3 y crea un entorno virtual:

  sudo apt install python3-venv
  python3 -m venv myenv
  source myenv/bin/activate

3.  Instala las dependencias necesarias:

  pip install --upgrade google-cloud-speech
  
4.  Configuración de Google Cloud

Regístrate en Google Cloud y crea un proyecto.
Google Cloud
Activa y configura la API Cloud Speech-to-Text:
Navega a la biblioteca de APIs y servicios y selecciona la Cloud Speech-to-Text API.
Activa la API y sigue los pasos para configurarla.
Crea una cuenta de servicio y descarga el archivo .json de credenciales:

export GOOGLE_APPLICATION_CREDENTIALS="/home/iot/transcripcion/credentials.json"
echo $GOOGLE_APPLICATION_CREDENTIALS

5.  Conversión de Video a Audio
Convierte el video .mp4 a archivos .wav en partes de 45 segundos:

ffmpeg -i video.mp4 -f segment -segment_time 45 -c copy output%03d.wav

6.  Convierte los archivos .wav de estéreo a mono:

chmod +x convert_to_mono.sh
./convert_to_mono.sh

7.  Ejecuta el script principal para iniciar la transcripción:

python main.py

Licencia
Este proyecto está liberado bajo la licencia Creative Commons Zero v1.0 Universal (CC0), lo que significa que puedes usar, copiar, modificar y distribuir este trabajo sin restricciones.

Soporte y Contribuciones
Si tienes preguntas o deseas contribuir al proyecto, no dudes en abrir un issue o un pull request en este repositorio. También puedes ver el video tutorial en mi canal de YouTube para obtener más detalles sobre la configuración y el uso del proyecto.
