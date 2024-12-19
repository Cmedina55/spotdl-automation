import os
import subprocess

def download_track(track_url):
    """
    Descarga una canción desde Spotify utilizando spotdl.
    """
    try:
        # Ejecutar el comando spotdl con la URL proporcionada
        subprocess.run(["spotdl", track_url], check=True)
        print(f"Descarga completada para: {track_url}")
    except subprocess.CalledProcessError as e:
        print(f"Error al descargar la canción: {e}")

if __name__ == "__main__":
    # URL de la canción en Spotify
    track_url = "https://open.spotify.com/intl-es/track/7CkJfQByYyFdu9jRRXk858"
    
    # Descargar la canción
    download_track(track_url)
