import subprocess
import sys
import os

def download_song(spotify_url):
    try:
        # Define output directory
        output_dir = "./downloads"
        os.makedirs(output_dir, exist_ok=True)

        # Run the SpotDL command
        command = [
            "spotdl",
            "download",
            "--output", output_dir,
            spotify_url
        ]
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print(result.stdout)
        print(f"Canción descargada exitosamente en {output_dir}.")
    except subprocess.CalledProcessError as e:
        print("Error al descargar la canción:")
        print(e.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py <Spotify URL>")
        sys.exit(1)

    spotify_url = sys.argv[1]
    print(f"Procesando la URL: {spotify_url}")
    download_song(spotify_url)
