import subprocess

def download_track(track_url):
    """
    Descarga una canción desde Spotify utilizando spotdl con detalles de depuración.
    """
    try:
        print(f"Procesando la URL: {track_url}")
        
        # Ejecutar el comando spotdl con argumentos de depuración para yt-dlp
        result = subprocess.run(
            ["spotdl", "--log-level", "DEBUG", track_url],  # Nivel DEBUG para logs detallados
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
        
        print("Comando ejecutado con éxito.")
        print("Salida estándar (stdout):")
        print(result.stdout)
        
    except subprocess.CalledProcessError as e:
        print("Error al descargar la canción:")
        print("Código de salida:", e.returncode)
        print("Salida estándar (stdout):")
        print(e.stdout)
        print("Salida de error (stderr):")
        print(e.stderr)
        
    except Exception as ex:
        print(f"Se produjo un error inesperado: {ex}")

if __name__ == "__main__":
    # URL de la canción en Spotify
    track_url = "https://open.spotify.com/intl-es/track/7CkJfQByYyFdu9jRRXk858"
    
    # Descargar la canción
    download_track(track_url)
