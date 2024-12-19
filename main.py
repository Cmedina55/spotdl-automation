import subprocess
import sys

def download_song(spotify_url):
    try:
        # Ejecutar el comando de descarga
        command = [
            "spotdl",
            "download",
            spotify_url
        ]
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print(result.stdout)  # Mostrar la salida de spotdl
        print("Canción descargada exitosamente.")
    except subprocess.CalledProcessError as e:
        # Capturar errores del comando
        print("Error al descargar la canción:")
        print(e.stderr)  # Mostrar errores de spotdl
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python main.py <URL de Spotify>")
        sys.exit(1)
    
    spotify_url = sys.argv[1]
    download_song(spotify_url)
