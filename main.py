import subprocess

def download_song(spotify_url):
    try:
        # Comando para ejecutar spotdl
        command = ["spotdl", "download", spotify_url]
        result = subprocess.run(command, capture_output=True, text=True)

        # Imprime la salida del comando
        if result.returncode == 0:
            print("Descarga completada correctamente.")
            print(result.stdout)
        else:
            print("Error al descargar la canción:")
            print(result.stderr)

    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    spotify_url = "https://open.spotify.com/intl-es/track/7CkJfQByYyFdu9jRRXk858"
    download_song(spotify_url)
