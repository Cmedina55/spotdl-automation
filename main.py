import os
import subprocess

def download_spotify_track(url):
    try:
        result = subprocess.run(['spotdl', url], check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

if __name__ == "__main__":
    track_url = "https://open.spotify.com/intl-es/track/7CkJfQByYyFdu9jRRXk858"
    download_spotify_track(track_url)
