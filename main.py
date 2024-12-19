import subprocess
import sys

def download_song(spotify_url):
    try:
        # Comando para descargar la canción con yt-dlp como backend
        command = [
            "spotdl",
            "download",
            spotify_url
        ]
        subprocess.run(command, check=True)
        print("Canción descargada exitosamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al descargar la canción: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python main.py <URL de Spotify>")
        sys.exit(1)
    
    spotify_url = sys.argv[1]
    download_song(spotify_url)
