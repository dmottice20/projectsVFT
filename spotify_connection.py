import os
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

# FILL OUT CLIENT AND SECRET ID EACH TIME FOR PRIVACY
cid = ""
secret = ""
os.environ['SPOTIPY_CLIENT_ID'] = cid
os.environ['SPOTIPY_CLIENT_SECRET'] = secret
os.environ['SPOTIPY_REDIRECT_URI'] = ""

username = 'davidmottice'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
scope = 'user-top-read'
auth_manager = SpotifyOAuth(scope=scope)
token_data = auth_manager.get_access_token()
token = token_data['access_token']

if token:
    sp = spotipy.Spotify(auth=token, client_credentials_manager=client_credentials_manager, auth_manager=auth_manager)
    # results = sp.new_releases(country="US", limit=50, offset=0)
    # results = sp.current_user_top_tracks(limit=50, offset=0, time_range='medium_term')
    # Shawn Mendes - spotify:artist:7n2wHs1TKAczGzO7Dd2rGr
    # The Wknd - spotify:artist:1Xyo4u8uXC1ZmMpatF05PJ
    # Brooks and Dunn - spotify:artist:0XKOBt59crntr7HQXXO8Yz
    # Drivers License - spotify:track:7lPN2DXiMsVn7XUKtOW1CS
    # Love Story (Taylor's Version) - spotify:track:3CeCwYWvdfXbZLXFhBrbnf
    results = sp.recommendations(seed_artists=['7n2wHs1TKAczGzO7Dd2rGr', '1Xyo4u8uXC1ZmMpatF05PJ'],
                                 seed_tracks=['7lPN2DXiMsVn7XUKtOW1CS', '3CeCwYWvdfXbZLXFhBrbnf'],
                                 seed_genres=sp.recommendation_genre_seeds(),
                                 country="US",
                                 limit=100)
    lst = [results]
    with open('generated_songs.json', 'w', encoding='utf-8') as f:
        json.dump(lst, f, ensure_ascii=False, indent=4)
else:
    print("Can't get token for", username)
