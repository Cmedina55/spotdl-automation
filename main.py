# main.py
import os

def download_spotify_track(url):
    os.system(f'spotdl "{url}"')

if __name__ == "__main__":
    track_url = "https://open.spotify.com/intl-es/track/7CkJfQByYyFdu9jRRXk858"
    download_spotify_track(track_url)
