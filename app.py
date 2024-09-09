from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#Loading env variables and setting up oath
load_dotenv()

def spot_authentication():
    spot_auth = SpotifyOAuth(
        client_id = os.getenv('CLIENT_ID'),
        client_secret = os.getenv('CLIENT_SECRET'),
        redirect_uri = os.getenv('REDIRECT_URI'),
        scope= "user-library-read user-read-playback-state user-modify-playback-state"
    )

    return spotipy.Spotify(auth_manager=spot_auth)

spot_ob = spot_authentication() 

def get_user_playlists(spot_ob):
    playlist_ids = []
    user_playlists = spot_ob.current_user_playlists()
    for playlist in user_playlists['items']:
        print("Playlist:", playlist['name'], " ID:", playlist['id'])
        playlist_ids.append(playlist['id'])

    return playlist_ids

playlist_ids = get_user_playlists(spot_ob)

get_user_playlists(spot_ob)


def get_tracks_from_playlists(spot_ob, playlist_ids):
    tracks = spot_ob.playlist_tracks(playlist_ids)