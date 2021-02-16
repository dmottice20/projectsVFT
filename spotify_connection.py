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
    #
    # Brooks and Dunn - spotify:artist:0XKOBt59crntr7HQXXO8Yz
    # Drivers License - spotify:track:7lPN2DXiMsVn7XUKtOW1CS
    # Love Story (Taylor's Version) - spotify:track:3CeCwYWvdfXbZLXFhBrbnf
    # TikTok song - spotify:track:2Wo6QQD1KMDWeFkkjLqwx5
    results = sp.recommendations(seed_artists=['7n2wHs1TKAczGzO7Dd2rGr', '0XKOBt59crntr7HQXXO8Yz'],
                                 seed_tracks=['7lPN2DXiMsVn7XUKtOW1CS', '2Wo6QQD1KMDWeFkkjLqwx5'],
                                 seed_genres=sp.recommendation_genre_seeds(),
                                 country="US",
                                 limit=100)
    lst = [results]
    with open('generated_songs.json', 'w', encoding='utf-8') as f:
        json.dump(lst, f, ensure_ascii=False, indent=4)
    # Loop through generated songs and grab the artist_ids
    artists = set()
    for track in results['tracks']:
        artists.add(track['artists'][0]['id'])
    # Grab all artist objects related to the generated_songs.json
    artists_lst = []
    artist_genres = dict()
    for artist_id in artists:
        artist = sp.artist(artist_id=artist_id)
        artists_lst.append(artist)
        artist_genres[artist['name']] = artist['genres']

    # Dump artist data into generated_artists.json
    with open('generated_artists.json', 'w', encoding='utf-8') as f:
        json.dump(artists_lst, f, ensure_ascii=False, indent=4)
    # Dump data into artist_genres.json for data manipulation
    with open('artist_genres.json', 'w', encoding='utf-8') as f:
        json.dump(artist_genres, f, ensure_ascii=False, indent=4)
else:
    print("Can't get token for", username)
