import argparse
from src.yt_download import DownloadManager

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--spotify_playlist", help="link or hash code to Spotify playlist")
    parser.add_argument("-y", "--yt_link", help="link or hash code to YouTube video")
    args = parser.parse_args()
    
    dl_manager = DownloadManager()
    
    if args.spotify_playlist:
        dl_manager.download_playlist(args.spotify_playlist)
        
    if args.yt_link:
        dl_manager.download_single_mp3(args.yt_link)