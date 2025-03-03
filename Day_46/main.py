from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

#scrap page

date = input("Which year do year do you want to travel to? Rype the date in this format YYYY-MM-DD: ")
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/", headers=header)

billboard_webpage = response.text
soup = BeautifulSoup(billboard_webpage, "html.parser")

t_and_a = []
artists = []
titles = [item.getText().strip() for item in soup.select(".o-chart-results-list__item h3")]
for item in soup.select(".o-chart-results-list__item span"):
    if item.getText().strip() and str(item.getText().strip()).isdigit() == False and item.getText().strip() != "NEW" and item.getText().strip() != "-":
        artists.append(item.getText().strip())

for index, item in enumerate(titles):
    dictionary = {
        "title" : titles[index],
        "artist": None
    }
    t_and_a.append(dictionary)

# Replace these with your own credentials
SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = "https://example.com"

# Define the scope of access
scope = 'playlist-modify-public'

# Create a SpotifyOAuth object
sp_oauth = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                        client_secret=SPOTIPY_CLIENT_SECRET,
                        redirect_uri=SPOTIPY_REDIRECT_URI,
                        scope=scope,
                        cache_path=None)

# Get the authorization URL
auth_url = sp_oauth.get_authorize_url()
print(f'Please navigate to the following URL to authorize: {auth_url}')

# After authorization, Spotify will redirect to the redirect URI with a code
response = input('Enter the URL you were redirected to: ')
code = sp_oauth.parse_response_code(response)

# Get the access token
token_info = sp_oauth.get_access_token(code)
access_token = token_info['access_token']

# Use the access token to create a Spotipy client
sp = spotipy.Spotify(auth=access_token)


# Function to get the URI of a song
def get_song_uri(song_name, artist_name=None, year=None):
    query = f"track:{song_name}"
    if artist_name:
        query += f" artist:{artist_name}"
    if year:
        query += f" year:{year}"

    result = sp.search(query, type='track', limit=1)
    if result['tracks']['items']:
        return result['tracks']['items'][0]['uri']
    else:
        return None



user_info = sp.current_user()

# Extract the username
username = user_info['id']
print(f"Current user's username: {username}")
playlist_name = f'AAA TEST {date} Billboard top 100'
playlist_description = f'This is a new playlist created with Spotipy. With hists from {date}'

playlist = sp.user_playlist_create(user=username, name=playlist_name, description=playlist_description)
print(f"Playlist created: {playlist['name']}")

uris = []
for song in t_and_a:
    song_name = song["title"]
    artist = song["artist"]
    uri = get_song_uri(song_name,artist)
    if uri:
        uris.append(uri)

print(uris)

playlist_id = playlist['id']

sp.playlist_add_items(playlist_id=playlist_id, items=uris)
print("Tracks added to the playlist.")