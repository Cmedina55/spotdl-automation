import subprocess
import sys

def download_with_cookies(track_url, browser="chrome"):
    """
    Descarga un video o canción utilizando yt-dlp con cookies desde el navegador.

    Args:
        track_url (str): URL del video o canción.
        browser (str): Navegador a usar para las cookies ('chrome' o 'firefox').

    Returns:
        tuple: stdout, stderr de la ejecución del comando.
    """
    command = [
        "yt-dlp",
        "--cookies-from-browser", browser,
        track_url
    ]

    print(f"Procesando la URL: {track_url}")
    result = subprocess.run(
        command,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return result.stdout, result.stderr


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py <URL>")
        sys.exit(1)

    track_url = sys.argv[1]
    browser = sys.argv[2] if len(sys.argv) > 2 else "chrome"

    stdout, stderr = download_with_cookies(track_url, browser)

    print("==== Salida del Comando ====")
    print(stdout)
    print("==== Errores (si los hay) ====")
    print(stderr)
