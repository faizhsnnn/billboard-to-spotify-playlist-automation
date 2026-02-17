from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# -------------------- GET DATE --------------------

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# -------------------- SCRAPE BILLBOARD --------------------

headers = {"User-Agent": "Mozilla/5.0"}
url = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
song_elements = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_elements]

# -------------------- SPOTIFY AUTH --------------------

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        redirect_uri="http://127.0.0.1:8888/callback",
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
print(f"Logged in as: {user_id}")

# -------------------- SEARCH SONGS --------------------

song_uris = []
year = date.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track", limit=1)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} not found. Skipped.")

# -------------------- CREATE PLAYLIST --------------------

playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False
)

# -------------------- ADD SONGS --------------------

sp.playlist_add_items(
    playlist_id=playlist["id"],
    items=song_uris
)

print("✅ Playlist created successfully!")
