import os

from . import get_credentials
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def setup_manager():
    client_id, client_secret = get_credentials()
    
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    return spotipy.Spotify(auth_manager)