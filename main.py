import sys
from spotdl import Spotdl
from yt_dlp import YoutubeDL
from spotdl.types.song import Song
from spotdl.utils.search import get_youtube_link
from spotdl.utils.ffmpeg import convert

# Configuración de SpotDL
spotdl_config = {
    "output": "{artists} - {title}.{output-ext}",
    "format": "mp3",
    "overwrite": "skip",
    "threads": 4,
    "search_query": None,
    "log_level": "DEBUG",
}

# Configuración de YT-DLP
ytdlp_options = {
    "format": "bestaudio/best",
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192",
    }],
    "quiet": False,
    "progress_hooks": [lambda d: print(d.get("status", "Downloading..."))],
}


def download_with_spotdl(url):
    try:
        spotdl = Spotdl(spotdl_config)
        song = Song.from_url(url)
        print(f"Descargando: {song.name} de {', '.join(song.artists)}")
        spotdl.download([song])
        print("Descarga completada con SpotDL")
    except Exception as e:
        print(f"Error con SpotDL: {str(e)}")
        download_with_ytdlp(url)


def download_with_ytdlp(url):
    try:
        with YoutubeDL(ytdlp_options) as ytdl:
            print(f"Descargando con YT-DLP: {url}")
            ytdl.download([url])
            print("Descarga completada con YT-DLP")
    except Exception as e:
        print(f"Error con YT-DLP: {str(e)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python main.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    print(f"Procesando la URL: {url}")

    if "spotify" in url:
        download_with_spotdl(url)
    elif "youtube" in url:
        download_with_ytdlp(url)
    else:
        print("Plataforma no soportada. Usa una URL de Spotify o YouTube.")
