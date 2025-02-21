import spotipy
import os
import random
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

'''''''''

# creates a random playlist from my_playlist_tracks.csv

# if (i display in a frontend app) {
    display the randomised playlists to shuffle in the background
    spotify playback sdk

    i would do user login but idk if i can in python within the timeframe lmao
}

'''''''''

def create_playlist(csv_file, playlist_name, tracks_num=10):

    df = pd.read_csv('data/my_playlist_tracks.csv')

    # auth and token
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id = os.getenv('SPOTIFY_CLIENT_ID'),
        client_secret = os.getenv('SPOTIFY_CLIENT_SECRET'),
        redirect_uri='http://localhost:8000/callback',
        scope='user-top-read, playlist-read-private, playlist-modify-public',
        #cache_path=cache_path
    ))

    user_id = sp.current_user()['id']
    
    # get track ids
    track_ids = df['track id'].tolist()

    # random selection
    selected_tracks = random.sample(track_ids, min(tracks_num, len(track_ids)))

    playlist_name = 'Random Playlist from AHS'
    playlist_description = f"Random playlist from {csv_file} with {tracks_num} tracks."
    playlist = sp.user_playlist_create(user_id, playlist_name, description=playlist_description)

    # add using uri
    track_uris = [f'spotify:track:{track_id}' for track_id in selected_tracks]
    sp.playlist_add_items(playlist['id'], track_uris)

    # done
    print(f'{playlist_name} created successfully!')

create_playlist('data/my_playlist_tracks.csv', playlist_name='Random Playlist from .csv', tracks_num=20)
