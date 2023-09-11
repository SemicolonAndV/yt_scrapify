import os
import re

from .scrape_spotify import setup_manager
from youtube_dl import YoutubeDL
from youtube_search import YoutubeSearch
import spotipy


class DownloadManager:
    def __init__(self):
        self.spotify: spotipy.Spotify = setup_manager()
        self.yt_dl_options: dict = {
            "format": "bestaudio/best",
            "ext": "mp3",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
            "outtmpl": f'{os.environ["USERPROFILE"]}/downloaded/%(title)s.%(ext)s',
        }
        self.yt_dl: YoutubeDL = YoutubeDL(self.yt_dl_options)
        
    def get_first_result(self, search_terms: str) -> dict:
        results = YoutubeSearch(search_terms, max_results=1).to_dict()
        
        return results[0]
    
    @staticmethod
    def parse_yt_link(url: str) -> str:
        # url has format '/watch?v={video_hash}'
        return f"https://youtube.com{url}"
    
    def download_single_mp3(self, link: str) -> None:
        yt_link = self.parse_yt_link(link)
        if not re.match(r'((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?',
                yt_link):
            print("Invalid URL")
        
        try:
            self.yt_dl.download(yt_link)
        except:
            print(f"Couldn't download video {yt_link}")
        
    def get_playlist_items(self, playlist_id: str) -> dict:
        return self.spotify.playlist(playlist_id)
    
    def download_playlist(self, playlist_id: str) -> None:
        
        for track in self.get_playlist_items(playlist_id).items():
            search_phrase = track["track"]["name"] + " " + track["track"]["artists"][0]["name"]
            
            yt_url = self.get_first_result(search_phrase)["url_suffix"]
            yt_url = self.parse_yt_link(yt_url)
            self.download_single_mp3(yt_url)