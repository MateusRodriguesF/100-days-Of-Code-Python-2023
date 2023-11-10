import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

artist_id = "7dGJo4pcD2V6oG8kP0tJRR"
#----------------------------------------------------------------
# user_date = input("Which year do you want to travel to? Type the date in this fortmat YYYY-MM-DD:\n")
# user_date = "1990-08-13"
# user_date_url = f"https://www.billboard.com/charts/hot-100/{user_date}"
#----------------------------------------------------------------
# response = requests.get(url=user_date_url)
# response.raise_for_status()


#----------------------------------------------------------------
# soup = BeautifulSoup(response.text, 'html.parser')
# song_names_spans = soup.select("li ul li h3")
# print(song_names_spans)
# song_names = [song.getText().strip() for song in song_names_spans]

# for song in song_names:
#     print(f"{song_names.index(song)+1}. {song}")
#----------------------------------------------------------------

# birdy_uri = f"spotify:artist:{artist_id}"
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(birdy_uri, album_type="album")
albums = results["items"]
while results["next"]:
    results = spotify.next(results)
    albums.extend(results["items"])

for album in albums:
    print(album["name"])

#------------------------------------------------------------------

#----------------------------------------------------------------1990