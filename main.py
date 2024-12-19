import os
import subprocess

def download_and_verify_song(spotify_url):
    try:
        # Define el directorio de descargas
        output_dir = "downloads"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Comando para ejecutar spotdl con carpeta de salida definida
        command = [
            "spotdl", "download", 
            "--output", f"{output_dir}/{{track-name}}.{{output-ext}}", 
            spotify_url
        ]
        
        # Ejecutar el comando
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Verifica si el comando se ejecutó correctamente
        if result.returncode != 0:
            print("Error al descargar la canción:")
            print(result.stderr)
            return False

        print("Descarga completada correctamente.")
        
        # Obtener el nombre del archivo esperado
        # Nota: Esto asume que spotdl usa un formato estándar para el nombre del archivo
        expected_file = os.path.join(output_dir, f"{spotify_url.split('/')[-1]}.mp3")

        # Verifica si el archivo existe en el directorio de descargas
        if not any(file.endswith(".mp3") for file in os.listdir(output_dir)):
            print(f"Error: No se encontró el archivo de audio esperado en {output_dir}.")
            return False

        print(f"Archivo descargado correctamente en {output_dir}.")
        return True

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return False


# Ejecutar la función con la URL de Spotify
spotify_url = "https://open.spotify.com/intl-es/track/7CkJfQByYyFdu9jRRXk858"
download_and_verify_song(spotify_url)
