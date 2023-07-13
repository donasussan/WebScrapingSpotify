import requests
from bs4 import BeautifulSoup
import pprint


Client_id = "5d7ce04406e04317aa78a381994cd8c8"
Client_secret = "5c3370f32db14c32a2c8fb88a27bb455"
Username = "313a62yednbmpu2bivxkdz463xem"
date = input("Enter a date you feel like travelling into! Type in YYYY-MM-DD format :)")
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}")
data = response.text
soup = BeautifulSoup(data, "html.parser")
titles = []
title_list = soup.find_all(name="h3", class_="a-no-trucate" )
for song in title_list:
    all_titles = song.get_text().strip()
    titles.append(all_titles)

print(titles)

#spotify authentication with spotipy
import spotipy
from spotipy.oauth2 import SpotifyOAuth


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=Client_id,
    client_secret=Client_secret,
    redirect_uri="http://example.com",
    scope="playlist-modify-private",
    cache_path ="token.txt",
    show_dialog=True,
    username= Username))

user_id = sp.current_user()["id"]
playlist_name = "2020-06-12"
playlist_description = "Love"

# Create the new playlist
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, description=playlist_description)

# Get the playlist ID
playlist_id = playlist["id"]
print(f"Playlist created! Playlist ID: {playlist_id}")

track_uris=[]
for title in titles:
    query = f'track:{title} year:{date.split("-")[0]}'
    # Perform search
    results = sp.search(q=query, type='track', limit=1)
    track_uri = results['tracks']['items'][0]['uri']
    track_uris.append(track_uri)

sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=track_uris, position=None)













